#!/usr/bin/env python3
"""Scrape beyondtheirdreams.com — pages, text, images, and asset metadata."""
import os, re, json, hashlib, time, urllib.parse as up
from pathlib import Path
import requests
from bs4 import BeautifulSoup

ROOT = "https://www.beyondtheirdreams.com/"
DOMAIN = up.urlparse(ROOT).netloc
OUT = Path(__file__).parent
PAGES_DIR = OUT / "pages"
IMG_DIR = OUT / "images"
TEXT_DIR = OUT / "text"
RAW_DIR = OUT / "raw_html"
for d in (PAGES_DIR, IMG_DIR, TEXT_DIR, RAW_DIR):
    d.mkdir(exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

session = requests.Session()
session.headers.update(HEADERS)

visited_pages = set()
queued = [ROOT]
all_images = {}   # url -> {alt, sources, local}
page_records = []

def safe_name(url):
    p = up.urlparse(url)
    path = p.path.strip("/").replace("/", "_") or "home"
    if p.query:
        path += "_" + hashlib.md5(p.query.encode()).hexdigest()[:6]
    return re.sub(r"[^A-Za-z0-9._-]", "_", path)[:120]

def is_internal(url):
    try:
        return up.urlparse(url).netloc in ("", DOMAIN)
    except Exception:
        return False

def absolutize(base, href):
    return up.urljoin(base, href)

def fetch(url):
    try:
        r = session.get(url, timeout=30, allow_redirects=True)
        if r.status_code == 200:
            return r
    except Exception as e:
        print(f"  ! fetch err {url}: {e}")
    return None

def download_image(url, alt, source_page):
    if url in all_images:
        all_images[url]["sources"].add(source_page)
        if alt and alt not in all_images[url]["alts"]:
            all_images[url]["alts"].append(alt)
        return
    parsed = up.urlparse(url)
    ext = os.path.splitext(parsed.path)[1].lower() or ".img"
    name = hashlib.md5(url.encode()).hexdigest()[:10] + "_" + safe_name(url)
    if not name.lower().endswith(ext):
        name += ext
    local = IMG_DIR / name
    if not local.exists():
        try:
            r = session.get(url, timeout=30)
            if r.status_code == 200 and r.content:
                local.write_bytes(r.content)
                print(f"  img: {name} ({len(r.content)//1024} KB)")
            else:
                print(f"  ! img status {r.status_code}: {url}")
                return
        except Exception as e:
            print(f"  ! img err {url}: {e}")
            return
    all_images[url] = {
        "url": url,
        "local": str(local.relative_to(OUT)),
        "alts": [alt] if alt else [],
        "sources": {source_page},
    }

def extract_text(soup):
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    parts = []
    # Headings + paragraphs + list items + buttons + links text
    for el in soup.find_all(["h1","h2","h3","h4","h5","h6","p","li","a","button","blockquote","figcaption","span"]):
        t = el.get_text(" ", strip=True)
        if not t:
            continue
        tag = el.name
        if tag.startswith("h"):
            parts.append(f"\n## [{tag.upper()}] {t}")
        elif tag == "li":
            parts.append(f"  - {t}")
        elif tag == "a":
            href = el.get("href","")
            parts.append(f"  [LINK -> {href}] {t}")
        elif tag == "button":
            parts.append(f"  [BUTTON] {t}")
        else:
            parts.append(t)
    # Dedupe consecutive duplicates (Squarespace often nests)
    out, prev = [], None
    for line in parts:
        if line != prev:
            out.append(line)
            prev = line
    return "\n".join(out)

def process_page(url):
    if url in visited_pages:
        return
    visited_pages.add(url)
    print(f"PAGE: {url}")
    r = fetch(url)
    if not r:
        return
    html = r.text
    base_name = safe_name(url) or "home"
    (RAW_DIR / f"{base_name}.html").write_text(html, encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")

    title = (soup.title.string.strip() if soup.title and soup.title.string else "")
    meta_desc = ""
    md = soup.find("meta", attrs={"name":"description"})
    if md: meta_desc = md.get("content","").strip()
    og = {m.get("property",""): m.get("content","") for m in soup.find_all("meta") if m.get("property","").startswith("og:")}

    # Images: <img src/srcset>, <source srcset>, inline style backgrounds, data-src
    img_count = 0
    candidates = []
    for img in soup.find_all("img"):
        src = img.get("src") or img.get("data-src") or img.get("data-image")
        srcset = img.get("srcset") or img.get("data-srcset") or ""
        alt = img.get("alt","").strip()
        if src:
            candidates.append((absolutize(url, src), alt))
        if srcset:
            # take the largest from srcset
            try:
                items = [s.strip() for s in srcset.split(",") if s.strip()]
                # parse "url w" pairs
                parsed_items = []
                for it in items:
                    bits = it.split()
                    if not bits: continue
                    u = bits[0]
                    w = 0
                    if len(bits) > 1 and bits[1].endswith("w"):
                        try: w = int(bits[1][:-1])
                        except: w = 0
                    parsed_items.append((u, w))
                if parsed_items:
                    parsed_items.sort(key=lambda x: x[1], reverse=True)
                    candidates.append((absolutize(url, parsed_items[0][0]), alt))
            except Exception:
                pass
    for src in soup.find_all("source"):
        srcset = src.get("srcset","")
        if srcset:
            u = srcset.split(",")[0].strip().split()[0]
            candidates.append((absolutize(url, u), ""))
    # Inline backgrounds
    for el in soup.find_all(style=True):
        s = el["style"]
        for m in re.finditer(r'url\(([^)]+)\)', s):
            u = m.group(1).strip().strip('"').strip("'")
            if u.startswith("data:"): continue
            candidates.append((absolutize(url, u), el.get("aria-label","").strip()))
    # data-src attributes anywhere
    for el in soup.find_all(attrs={"data-src": True}):
        u = el.get("data-src")
        if u and not u.startswith("data:"):
            candidates.append((absolutize(url, u), el.get("alt","").strip()))

    seen = set()
    for u, alt in candidates:
        if not u or u in seen: continue
        seen.add(u)
        # Filter — keep only http(s)
        if not u.startswith("http"):
            continue
        download_image(u, alt, url)
        img_count += 1

    text = extract_text(soup)
    text_path = TEXT_DIR / f"{base_name}.md"
    header = f"# {title}\nURL: {url}\nDescription: {meta_desc}\n\n"
    text_path.write_text(header + text, encoding="utf-8")

    page_records.append({
        "url": url,
        "title": title,
        "description": meta_desc,
        "og": og,
        "image_count": img_count,
        "text_file": str(text_path.relative_to(OUT)),
        "html_file": str((RAW_DIR / f"{base_name}.html").relative_to(OUT)),
    })

    # Discover internal links
    for a in soup.find_all("a", href=True):
        href = absolutize(url, a["href"])
        # strip fragment
        href = href.split("#")[0]
        if not is_internal(href): continue
        # only http(s)
        p = up.urlparse(href)
        if p.scheme not in ("http","https"): continue
        # skip files
        if re.search(r"\.(pdf|jpg|jpeg|png|gif|webp|svg|mp4|mov|zip|css|js|ico)$", p.path, re.I):
            continue
        if href not in visited_pages and href not in queued:
            queued.append(href)

while queued:
    url = queued.pop(0)
    process_page(url)
    time.sleep(0.5)

# Save manifest
manifest = {
    "root": ROOT,
    "page_count": len(page_records),
    "image_count": len(all_images),
    "pages": page_records,
    "images": [
        {
            "url": k,
            "local": v["local"],
            "alts": v["alts"],
            "sources": sorted(v["sources"]),
        } for k, v in all_images.items()
    ],
}
(OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print(f"\nDone. {len(page_records)} pages, {len(all_images)} images.")
