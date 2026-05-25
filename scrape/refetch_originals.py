#!/usr/bin/env python3
"""Re-scan saved HTML for image URLs, strip Wix transform suffixes,
download originals at full resolution with proper Referer."""
import os, re, json, hashlib, urllib.parse as up
from pathlib import Path
import requests
from bs4 import BeautifulSoup

OUT = Path(__file__).parent
RAW = OUT / "raw_html"
IMG = OUT / "images_originals"
IMG.mkdir(exist_ok=True)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Referer": "https://www.beyondtheirdreams.com/",
    "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
}

session = requests.Session()
session.headers.update(HEADERS)

def strip_wix_transform(url):
    """For Wix static media URLs, strip /v1/... to get the original."""
    if "wixstatic.com/media/" not in url:
        return url
    # Cut at /v1/
    i = url.find("/v1/")
    if i == -1:
        return url
    return url[:i]

def collect_urls():
    urls = {}  # original_url -> {alt, sources:set}
    for f in RAW.glob("*.html"):
        soup = BeautifulSoup(f.read_text(encoding="utf-8"), "lxml")
        page = f.stem
        cands = []
        for img in soup.find_all("img"):
            for attr in ("src","data-src","data-pin-media","data-image"):
                v = img.get(attr)
                if v: cands.append((v, img.get("alt","").strip()))
            ss = img.get("srcset") or img.get("data-srcset") or ""
            if ss:
                for it in ss.split(","):
                    bits = it.strip().split()
                    if bits: cands.append((bits[0], img.get("alt","").strip()))
        for src in soup.find_all("source"):
            ss = src.get("srcset","")
            for it in ss.split(","):
                bits = it.strip().split()
                if bits: cands.append((bits[0], ""))
        for el in soup.find_all(style=True):
            for m in re.finditer(r'url\(([^)]+)\)', el["style"]):
                u = m.group(1).strip().strip('"').strip("'")
                if not u.startswith("data:"): cands.append((u, ""))
        # Anywhere in HTML — last-resort regex catch
        html = f.read_text(encoding="utf-8")
        for m in re.finditer(r'https?://static\.wixstatic\.com/media/[^\s"\'\)<>]+', html):
            cands.append((m.group(0), ""))

        for u, alt in cands:
            if not u.startswith("http"): continue
            orig = strip_wix_transform(u)
            rec = urls.setdefault(orig, {"alts": [], "sources": set()})
            if alt and alt not in rec["alts"]: rec["alts"].append(alt)
            rec["sources"].add(page)
    return urls

def safe_name(url):
    p = up.urlparse(url)
    base = os.path.basename(p.path) or "img"
    h = hashlib.md5(url.encode()).hexdigest()[:8]
    base = re.sub(r"[^A-Za-z0-9._~-]", "_", base)
    return f"{h}_{base}"

def download(url):
    name = safe_name(url)
    # Determine extension from URL or content-type later
    local = IMG / name
    # If file already exists with content, skip
    if local.exists() and local.stat().st_size > 0:
        return local, "cached"
    try:
        r = session.get(url, timeout=45, stream=True)
        if r.status_code == 200:
            ct = r.headers.get("content-type","").lower()
            ext = ""
            if "jpeg" in ct or "jpg" in ct: ext = ".jpg"
            elif "png" in ct: ext = ".png"
            elif "webp" in ct: ext = ".webp"
            elif "gif" in ct: ext = ".gif"
            elif "svg" in ct: ext = ".svg"
            elif "avif" in ct: ext = ".avif"
            if ext and not local.suffix:
                local = local.with_suffix(ext)
            local.write_bytes(r.content)
            return local, f"ok {len(r.content)//1024}KB"
        else:
            return None, f"status {r.status_code}"
    except Exception as e:
        return None, f"err {e}"

def main():
    urls = collect_urls()
    print(f"Discovered {len(urls)} unique original URLs")
    results = []
    ok = 0; fail = 0
    for url, meta in sorted(urls.items()):
        local, status = download(url)
        results.append({
            "url": url,
            "local": str(local.relative_to(OUT)) if local else None,
            "status": status,
            "alts": meta["alts"],
            "sources": sorted(meta["sources"]),
        })
        if local: ok += 1
        else: fail += 1
        print(f"{status:>14}  {url[:120]}")
    (OUT / "originals_manifest.json").write_text(
        json.dumps({"count": len(results), "ok": ok, "fail": fail, "items": results}, indent=2),
        encoding="utf-8")
    print(f"\nDone. ok={ok} fail={fail}")

if __name__ == "__main__":
    main()
