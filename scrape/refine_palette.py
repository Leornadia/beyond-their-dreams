#!/usr/bin/env python3
"""Refine the styles report:
- Dedupe @font-face declarations.
- Isolate brand colors from Wix system defaults by parsing CSS custom properties
  (--color_1..--color_36, --brand-* tokens) and by ignoring known Wix UI colors.
"""
import re, json
from pathlib import Path
from collections import Counter

OUT = Path(__file__).parent
combined = (OUT / "css" / "_combined.css").read_text(encoding="utf-8")

# ---------- Wix theme tokens ----------
# Wix exposes theme palette as --color_1..--color_36
theme_tokens = {}
for m in re.finditer(r'--color_(\d+)\s*:\s*([^;}]+)\s*[;}]', combined):
    n = int(m.group(1))
    val = m.group(2).strip()
    # Keep the most frequent value if multiple definitions
    theme_tokens.setdefault(n, Counter())[val] += 1

# Resolve to most common value per slot
resolved_theme = {}
for n, ctr in sorted(theme_tokens.items()):
    val, _ = ctr.most_common(1)[0]
    resolved_theme[n] = val

# Custom theme color variables (brand tokens)
brand_vars = {}
for m in re.finditer(r'(--(?:brand|primary|secondary|accent|text|bg|background)[A-Za-z0-9_-]*)\s*:\s*([^;}]+)\s*[;}]', combined, re.I):
    name = m.group(1)
    val = m.group(2).strip()
    brand_vars.setdefault(name, Counter())[val] += 1
brand_vars = {k: v.most_common(1)[0][0] for k,v in brand_vars.items()}

# ---------- Known Wix UI defaults to flag ----------
WIX_UI = {
    "#116dff", "#3899ec", "#ff4040", "#7fccf7", "#373b4d", "#edf0f2",
    "#fafafa", "#eeeeee", "#e0e0e0", "#dbdbdb", "#e2e2e2", "#e8e8e8",
    "#000000", "#ffffff", "#525252", "#7a7a7a", "#393939",
}

# ---------- Re-extract colors from styles_manifest ----------
manifest = json.load(open(OUT / "styles_manifest.json"))
all_colors = manifest["color_counts"]  # list of [color, count]

brand_candidates = []
wix_ui = []
for col, n in all_colors:
    base = col.split("@")[0]
    if base in WIX_UI:
        wix_ui.append((col, n))
    else:
        brand_candidates.append((col, n))

# ---------- Dedupe font-faces ----------
seen = set()
unique_faces = []
for ff in manifest["font_faces"]:
    key = (ff["family"].lower(), ff["weight"], ff["style"])
    if key in seen: continue
    seen.add(key)
    unique_faces.append(ff)

# Filter font usage to families that look like real choices (skip Wix wf_* placeholders)
real_families = [(f, n) for f, n in manifest["font_family_uses"]
                 if not f.startswith("wf_") and not f.startswith("wfont_")
                 and f.lower() not in ("arial","helvetica")]

# ---------- Write refined PALETTE.md ----------
lines = []
lines.append("# Beyond Their Dreams — Brand Palette & Type System\n")
lines.append("Refined from inline CSS on `https://www.beyondtheirdreams.com/`. ")
lines.append("Wix editor UI defaults are flagged separately so they don't pollute the brand palette.\n")

def to_hex(val):
    """Convert various color formats (incl. raw 'r,g,b' triples) to #rrggbb."""
    val = val.strip()
    mh = re.fullmatch(r'#([0-9a-fA-F]{3,8})', val)
    if mh:
        c = mh.group(1)
        if len(c) == 3:  return "#" + "".join(ch*2 for ch in c).lower()
        if len(c) == 6:  return "#" + c.lower()
        if len(c) == 8:  return "#" + c[:6].lower()
    mr = re.fullmatch(r'rgba?\(\s*([^)]+)\)', val, re.I)
    if mr: val = mr.group(1)
    parts = [p.strip() for p in re.split(r'[,\s/]+', val) if p.strip()]
    try:
        if len(parts) >= 3:
            r,g,b = (int(round(float(p.rstrip('%')) * (255/100))) if p.endswith('%')
                     else int(round(float(p))) for p in parts[:3])
            return "#{:02x}{:02x}{:02x}".format(max(0,min(255,r)),max(0,min(255,g)),max(0,min(255,b)))
    except Exception:
        return ""
    return ""

# Build hex-keyed canonical theme: dedupe Wix's many duplicate slots
theme_hex = {}  # hex -> [slot numbers]
for n in sorted(resolved_theme):
    hx = to_hex(resolved_theme[n])
    if hx:
        theme_hex.setdefault(hx, []).append(f"--color_{n}")

# Order canonical palette by darkness (light -> dark) within hue families
def luminance(h):
    h = h.lstrip('#')
    r,g,b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    return 0.299*r + 0.587*g + 0.114*b

lines.append("## Wix theme palette — canonical brand colors\n")
lines.append("Wix stores 60+ slots, mostly duplicates. Below is the deduplicated palette the site is actually built from.\n")
lines.append("| Swatch | Hex | Wix slot(s) |")
lines.append("|---|---|---|")
for hx in sorted(theme_hex.keys(), key=luminance, reverse=True):
    sw = f'<span style="display:inline-block;width:24px;height:24px;background:{hx};border:1px solid #999"></span>'
    slots = ", ".join(theme_hex[hx][:6]) + ("…" if len(theme_hex[hx])>6 else "")
    lines.append(f"| {sw} | `{hx}` | {slots} |")
lines.append("")

lines.append("<details><summary>All 60+ raw Wix slots</summary>\n")
lines.append("| Slot | Swatch | Hex | Raw value |\n|---|---|---|---|")
for n in sorted(resolved_theme):
    val = resolved_theme[n]
    hx = to_hex(val)
    sw = f'<span style="display:inline-block;width:18px;height:18px;background:{hx};border:1px solid #999"></span>' if hx else ""
    lines.append(f"| `--color_{n}` | {sw} | `{hx}` | `{val}` |")
lines.append("\n</details>\n")

if brand_vars:
    lines.append("## Other brand-named CSS variables\n")
    lines.append("| Variable | Value |\n|---|---|")
    for k, v in sorted(brand_vars.items()):
        lines.append(f"| `{k}` | `{v}` |")
    lines.append("")

lines.append("## Likely brand colors (excluding Wix UI defaults)\n")
lines.append("Colors that appear in the CSS but are NOT in the Wix editor's default UI palette — these are the genuine brand choices.\n")
lines.append("| Swatch | Hex | Count | Likely role |")
lines.append("|---|---|---|---|")
# Heuristic role labels
def role_for(hex_):
    h = hex_.lstrip("#")[:6]
    if not re.fullmatch(r'[0-9a-fA-F]{6}', h): return ""
    r,g,b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    L = (0.299*r + 0.587*g + 0.114*b)
    if L > 235: return "near-white / background"
    if L < 25: return "near-black / text"
    # Detect warm browns
    if r > g > b and r-b > 30: return "warm / brown / tan"
    if g > r and g > b: return "green / sage"
    if b > r and b > g: return "blue (likely Wix default)"
    if abs(r-g) < 10 and abs(g-b) < 10: return "neutral / grey"
    return ""

for col, n in brand_candidates[:50]:
    base = col.split("@")[0]
    sw = f'<span style="display:inline-block;width:18px;height:18px;background:{base};border:1px solid #999"></span>'
    lines.append(f"| {sw} | `{col}` | {n} | {role_for(base)} |")
lines.append("")

lines.append("## Wix UI defaults present (informational — not brand)\n")
lines.append("| Swatch | Hex | Count |")
lines.append("|---|---|---|")
for col, n in wix_ui:
    base = col.split("@")[0]
    sw = f'<span style="display:inline-block;width:18px;height:18px;background:{base};border:1px solid #999"></span>'
    lines.append(f"| {sw} | `{col}` | {n} |")
lines.append("")

lines.append("## Type system (deduped)\n")
lines.append("### Real font families in use\n")
lines.append("| Family | Usage count |\n|---|---|")
for f, n in real_families[:20]:
    lines.append(f"| `{f}` | {n} |")
lines.append("")

lines.append("### Unique @font-face declarations\n")
lines.append("Each family/weight/style is listed once.\n")
lines.append("| Family | Weight | Style | Source file(s) |\n|---|---|---|---|")
for ff in unique_faces:
    srcs = ", ".join(s.split("/")[-1] for s in ff["src"])
    lines.append(f"| {ff['family']} | {ff['weight']} | {ff['style']} | {srcs} |")
lines.append("")

lines.append("## Files\n")
lines.append("- `css/_combined.css` — every inline + linked stylesheet glued together for analysis")
lines.append("- `fonts/` — all downloaded font files")
lines.append("- `styles_manifest.json` — raw machine-readable manifest")
lines.append("- `PALETTE.md` — full unfiltered report")
lines.append("- `BRAND.md` — this refined report (use this for the redesign)")

(OUT / "BRAND.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote BRAND.md")
print(f"Wix theme slots filled: {len(resolved_theme)}")
print(f"Brand color candidates: {len(brand_candidates)}")
print(f"Unique @font-face entries: {len(unique_faces)}")
print(f"Real font families: {len(real_families)}")
