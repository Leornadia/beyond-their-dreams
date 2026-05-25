#!/usr/bin/env python3
"""Discover, download, and analyze the site's CSS, fonts, and color palette."""
import os, re, json, hashlib, urllib.parse as up
from pathlib import Path
from collections import Counter, defaultdict
import requests
from bs4 import BeautifulSoup

OUT = Path(__file__).parent
RAW = OUT / "raw_html"
CSS_DIR = OUT / "css"
FONT_DIR = OUT / "fonts"
CSS_DIR.mkdir(exist_ok=True)
FONT_DIR.mkdir(exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Referer": "https://www.beyondtheirdreams.com/",
    "Accept": "text/css,*/*;q=0.1",
}
session = requests.Session()
session.headers.update(HEADERS)

ROOT = "https://www.beyondtheirdreams.com/"

# ---------- Discover ----------
css_urls = set()
inline_styles = []   # (page, css)
font_link_urls = set()

for f in sorted(RAW.glob("*.html")):
    soup = BeautifulSoup(f.read_text(encoding="utf-8"), "lxml")
    for link in soup.find_all("link"):
        rel = link.get("rel") or []
        href = link.get("href") or ""
        if not href: continue
        absurl = up.urljoin(ROOT, href)
        as_attr = link.get("as","")
        if "stylesheet" in rel or as_attr == "style" or href.endswith(".css"):
            css_urls.add(absurl)
        if as_attr == "font" or any(href.lower().endswith(ext) for ext in (".woff2",".woff",".ttf",".otf",".eot")):
            font_link_urls.add(absurl)
        # Google fonts / etc
        if "fonts.googleapis.com" in absurl or "fonts.gstatic.com" in absurl or "static.parastorage.com/services/santa-resources/dist/viewer/user-site-fonts" in absurl:
            css_urls.add(absurl)
    for style in soup.find_all("style"):
        if style.string:
            inline_styles.append((f.stem, style.string))
    # Inline style attributes are captured via the all-CSS string later

print(f"Discovered {len(css_urls)} CSS URLs, {len(font_link_urls)} font link URLs, {len(inline_styles)} inline <style> blocks")

# ---------- Download CSS ----------
css_records = []
all_css_text = []   # combined for color/font analysis

def safe_name(url, ext_hint=""):
    h = hashlib.md5(url.encode()).hexdigest()[:8]
    base = os.path.basename(up.urlparse(url).path) or "file"
    base = re.sub(r"[^A-Za-z0-9._~-]", "_", base)
    if ext_hint and not base.endswith(ext_hint):
        base += ext_hint
    return f"{h}_{base}"

def fetch(url, accept=None):
    h = dict(HEADERS)
    if accept: h["Accept"] = accept
    try:
        r = session.get(url, headers=h, timeout=45)
        return r
    except Exception as e:
        return None

for url in sorted(css_urls):
    r = fetch(url, accept="text/css,*/*;q=0.1")
    if not r or r.status_code != 200:
        print(f"  ! CSS fail {r.status_code if r else 'err'}: {url}")
        continue
    text = r.text
    name = safe_name(url, ".css")
    if not name.endswith(".css"): name += ".css"
    (CSS_DIR / name).write_text(text, encoding="utf-8")
    css_records.append({"url": url, "local": f"css/{name}", "bytes": len(text)})
    all_css_text.append(text)
    print(f"  css: {name} ({len(text)//1024} KB)")

for stem, txt in inline_styles:
    all_css_text.append(txt)
    (CSS_DIR / f"inline_{stem}.css").write_text(txt, encoding="utf-8")

# Capture inline style="" too — search raw html
inline_attr_blob = []
for f in RAW.glob("*.html"):
    html = f.read_text(encoding="utf-8")
    inline_attr_blob.extend(re.findall(r'style="([^"]+)"', html))
inline_attr_css = "\n".join(inline_attr_blob)
all_css_text.append(inline_attr_css)

combined = "\n\n/* ====== */\n\n".join(all_css_text)
(CSS_DIR / "_combined.css").write_text(combined, encoding="utf-8")
print(f"Combined CSS for analysis: {len(combined)//1024} KB")

# ---------- Follow @import + url(...) for fonts ----------
font_urls = set(font_link_urls)
for m in re.finditer(r'url\(\s*["\']?([^"\')\s]+\.(?:woff2|woff|ttf|otf|eot))(?:[?#][^"\')]*)?["\']?\s*\)', combined, re.I):
    u = m.group(1)
    if u.startswith("//"): u = "https:" + u
    elif u.startswith("/"): u = up.urljoin(ROOT, u)
    elif not u.startswith("http"): continue
    font_urls.add(u)
# @import urls — fetch and append their content
for m in re.finditer(r'@import\s+(?:url\()?\s*["\']?([^"\')]+)["\']?\s*\)?\s*;', combined):
    u = m.group(1)
    if u.startswith("//"): u = "https:" + u
    if u.startswith("http"):
        r = fetch(u, accept="text/css,*/*;q=0.1")
        if r and r.status_code == 200:
            (CSS_DIR / safe_name(u, ".css")).write_text(r.text, encoding="utf-8")
            combined += "\n" + r.text
            for m2 in re.finditer(r'url\(\s*["\']?([^"\')\s]+\.(?:woff2|woff|ttf|otf|eot))', r.text, re.I):
                u2 = m2.group(1)
                if u2.startswith("//"): u2 = "https:" + u2
                if u2.startswith("http"): font_urls.add(u2)
            print(f"  @import css: {u}")

# ---------- Download fonts ----------
font_records = []
for url in sorted(font_urls):
    r = fetch(url, accept="*/*")
    if not r or r.status_code != 200:
        print(f"  ! font fail {r.status_code if r else 'err'}: {url}")
        continue
    name = safe_name(url)
    (FONT_DIR / name).write_bytes(r.content)
    font_records.append({"url": url, "local": f"fonts/{name}", "bytes": len(r.content)})
    print(f"  font: {name} ({len(r.content)//1024} KB)")

# ---------- Analyze fonts ----------
font_faces = []
for m in re.finditer(r'@font-face\s*\{([^}]+)\}', combined, re.I | re.S):
    block = m.group(1)
    family = (re.search(r'font-family\s*:\s*([^;]+);', block, re.I) or [None,""])[1].strip().strip('"\'')
    weight = (re.search(r'font-weight\s*:\s*([^;]+);', block, re.I) or [None,""])[1].strip()
    style  = (re.search(r'font-style\s*:\s*([^;]+);', block, re.I) or [None,""])[1].strip()
    srcs   = re.findall(r'url\(\s*["\']?([^"\')\s]+)["\']?\s*\)', block)
    font_faces.append({"family": family, "weight": weight, "style": style, "src": srcs})

font_family_uses = Counter()
for m in re.finditer(r'font-family\s*:\s*([^;}{]+)[;}]', combined, re.I):
    stack = m.group(1).strip()
    # split, take first
    first = stack.split(",")[0].strip().strip('"\'')
    if first and not first.startswith("var("):
        font_family_uses[first] += 1

# ---------- Analyze colors ----------
color_counts = Counter()

# Hex
for m in re.finditer(r'#([0-9a-fA-F]{3,8})\b', combined):
    code = m.group(1)
    if len(code) in (3,4,6,8):
        # Normalize 3-digit to 6-digit, keep alpha if present
        if len(code) == 3:
            full = "".join(c*2 for c in code).lower()
            color_counts[f"#{full}"] += 1
        elif len(code) == 4:
            full = "".join(c*2 for c in code).lower()
            color_counts[f"#{full}"] += 1
        else:
            color_counts[f"#{code.lower()}"] += 1

# rgb / rgba
for m in re.finditer(r'rgba?\(\s*([0-9.\s,/%]+)\)', combined, re.I):
    body = m.group(1)
    parts = re.split(r'[,\s/]+', body.strip())
    parts = [p for p in parts if p]
    try:
        if len(parts) >= 3:
            r_,g_,b_ = (int(round(float(p.rstrip('%')) * (255/100))) if p.endswith('%')
                        else int(round(float(p))) for p in parts[:3])
            a_ = 1.0
            if len(parts) >= 4:
                ap = parts[3]
                a_ = float(ap.rstrip('%'))/100 if ap.endswith('%') else float(ap)
            hex_ = "#{:02x}{:02x}{:02x}".format(max(0,min(255,r_)), max(0,min(255,g_)), max(0,min(255,b_)))
            if abs(a_ - 1.0) < 0.001:
                color_counts[hex_] += 1
            else:
                color_counts[f"{hex_}@{a_:.2f}"] += 1
    except Exception:
        pass

# hsl / hsla
def hsl_to_hex(h, s, l):
    s/=100; l/=100
    c = (1-abs(2*l-1))*s
    x = c*(1-abs((h/60)%2 - 1))
    m_ = l - c/2
    if   h<60:  rp,gp,bp = c,x,0
    elif h<120: rp,gp,bp = x,c,0
    elif h<180: rp,gp,bp = 0,c,x
    elif h<240: rp,gp,bp = 0,x,c
    elif h<300: rp,gp,bp = x,0,c
    else:       rp,gp,bp = c,0,x
    return "#{:02x}{:02x}{:02x}".format(int(round((rp+m_)*255)), int(round((gp+m_)*255)), int(round((bp+m_)*255)))

for m in re.finditer(r'hsla?\(\s*([0-9.\s,/%deg]+)\)', combined, re.I):
    parts = re.split(r'[,\s/]+', m.group(1).strip())
    parts = [p for p in parts if p]
    try:
        if len(parts) >= 3:
            h = float(parts[0].replace('deg',''))
            s = float(parts[1].rstrip('%'))
            l = float(parts[2].rstrip('%'))
            a = 1.0
            if len(parts) >= 4:
                ap = parts[3]
                a = float(ap.rstrip('%'))/100 if ap.endswith('%') else float(ap)
            hx = hsl_to_hex(h%360, s, l)
            if abs(a-1.0) < 0.001:
                color_counts[hx] += 1
            else:
                color_counts[f"{hx}@{a:.2f}"] += 1
    except Exception:
        pass

# Save artifacts
(OUT / "styles_manifest.json").write_text(json.dumps({
    "css_files": css_records,
    "fonts_files": font_records,
    "font_faces": font_faces,
    "font_family_uses": font_family_uses.most_common(),
    "color_counts": color_counts.most_common(),
}, indent=2), encoding="utf-8")

# ---------- PALETTE.md ----------
lines = []
lines.append("# Beyond Their Dreams — Styles, Fonts, and Color Palette\n")
lines.append(f"Source: {ROOT}\n")
lines.append(f"- CSS files downloaded: {len(css_records)}")
lines.append(f"- Inline <style> blocks captured: {len(inline_styles)}")
lines.append(f"- Font files downloaded: {len(font_records)}")
lines.append(f"- @font-face declarations: {len(font_faces)}")
lines.append(f"- Distinct colors (incl. alpha variants): {len(color_counts)}\n")

lines.append("## Fonts in use (by frequency in CSS)\n")
lines.append("| Family | Usage count |")
lines.append("|---|---|")
for fam, n in font_family_uses.most_common(30):
    lines.append(f"| `{fam}` | {n} |")
lines.append("")

lines.append("## @font-face declarations\n")
for ff in font_faces[:200]:
    src_short = ", ".join(s.split('/')[-1] for s in ff['src'])
    lines.append(f"- **{ff['family']}** — weight `{ff['weight']}`, style `{ff['style']}` — files: {src_short}")
lines.append("")

lines.append("## Color palette (top 80, by frequency)\n")
lines.append("Each color is shown as a hex code with the count of times it appears in the site's CSS (inline + linked).")
lines.append("Alpha variants are flagged with `@<alpha>`.\n")
lines.append("| Swatch | Hex | Count |")
lines.append("|---|---|---|")
for col, n in color_counts.most_common(80):
    base = col.split("@")[0]
    lines.append(f"| <span style=\"display:inline-block;width:18px;height:18px;background:{base};border:1px solid #999\"></span> | `{col}` | {n} |")
lines.append("")

lines.append("## Files\n")
lines.append("- `css/` — all stylesheets (linked, inline, @imported)")
lines.append("- `css/_combined.css` — single file used for analysis")
lines.append("- `fonts/` — actual font files (woff2/woff/ttf/otf)")
lines.append("- `styles_manifest.json` — machine-readable manifest of everything above")
(OUT / "PALETTE.md").write_text("\n".join(lines), encoding="utf-8")

print(f"\nDone. {len(css_records)} CSS, {len(font_records)} fonts, {len(color_counts)} distinct colors.")
print("Wrote PALETTE.md and styles_manifest.json")
