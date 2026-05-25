#!/usr/bin/env python3
"""Build a single human-readable index.md tying pages to their text + images."""
import json
from pathlib import Path
from collections import defaultdict

OUT = Path(__file__).parent
manifest = json.load(open(OUT / "manifest.json"))
originals = json.load(open(OUT / "originals_manifest.json"))

# Map page-stem -> [original image local paths]
page_to_images = defaultdict(list)
for item in originals["items"]:
    if not item["local"]: continue
    for src in item["sources"]:
        page_to_images[src].append({
            "local": item["local"],
            "url": item["url"],
            "alts": item["alts"],
        })

lines = []
lines.append("# Beyond Their Dreams — Site Scrape Index\n")
lines.append(f"Scraped from {manifest['root']}\n")
lines.append(f"- Pages: {manifest['page_count']}")
lines.append(f"- Original images: {originals['ok']} (full-resolution, {sum(1 for _ in (OUT / 'images_originals').iterdir())} files)")
lines.append("")
lines.append("## Directory layout")
lines.append("")
lines.append("- `text/` — plain-text content extracted per page (markdown)")
lines.append("- `raw_html/` — full HTML source per page (for reference)")
lines.append("- `images_originals/` — full-resolution originals (Wix transforms stripped)")
lines.append("- `images/` — first-pass downloads (smaller variants, mostly transformed)")
lines.append("- `manifest.json` — page + image metadata from first crawl")
lines.append("- `originals_manifest.json` — original-image manifest with alts and source pages")
lines.append("")
lines.append("## Pages")
lines.append("")

# Map url to text-file stem
for p in manifest["pages"]:
    url = p["url"]
    text_rel = p.get("text_file","")
    text_stem = Path(text_rel).stem if text_rel else ""
    images = page_to_images.get(text_stem, [])
    lines.append(f"### {p['title'] or url}")
    lines.append(f"- URL: {url}")
    if p.get("description"):
        lines.append(f"- Meta: {p['description']}")
    if text_rel:
        lines.append(f"- Text: [{text_rel}]({text_rel})")
    lines.append(f"- HTML: [{p['html_file']}]({p['html_file']})")
    if images:
        lines.append(f"- Images on this page ({len(images)}):")
        for img in images:
            alt = img["alts"][0] if img["alts"] else ""
            lines.append(f"  - `{img['local']}`" + (f" — alt: \"{alt}\"" if alt else ""))
    lines.append("")

(OUT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote INDEX.md ({len(lines)} lines)")
