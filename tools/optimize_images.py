#!/usr/bin/env python3
"""Turn the source assets into web-ready images in assets/img/.

Usage:  python tools/optimize_images.py [SOURCE_DIR]
Default SOURCE_DIR: C:/Users/User/Dropbox/Assets
Requires Pillow (pip install pillow).
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "C:/Users/User/Dropbox/Assets")
OUT = Path(__file__).resolve().parent.parent / "assets" / "img"
OUT.mkdir(parents=True, exist_ok=True)


def white_to_alpha(im: Image.Image) -> Image.Image:
    """'Color to alpha' for a white background, keeping anti-aliased edges smooth."""
    im = im.convert("RGB")
    px = im.load()
    out = Image.new("RGBA", im.size)
    opx = out.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = px[x, y]
            a = max(255 - r, 255 - g, 255 - b)
            if a < 8:
                opx[x, y] = (255, 255, 255, 0)
                continue
            f = 255 / a
            opx[x, y] = tuple(min(255, max(0, round(255 - (255 - c) * f))) for c in (r, g, b)) + (a,)
    return out


def save_pair(im: Image.Image, stem: str, jpg_q: int = 72, webp_q: int = 70) -> None:
    im = im.convert("RGB")
    im.save(OUT / f"{stem}.jpg", "JPEG", quality=jpg_q, optimize=True, progressive=True)
    im.save(OUT / f"{stem}.webp", "WEBP", quality=webp_q, method=6)


# Logo: transparent PNG so it sits cleanly on the transparent header.
logo = white_to_alpha(Image.open(SRC / "thomasmoor.org.logo220x46.jpg"))
logo.save(OUT / "logo.png", optimize=True)

# Favicons: crop the mark to a padded square.
fav = Image.open(SRC / "thomasmoor.org.favicon.jpeg").convert("RGB")
bbox = ImageOps.invert(fav.convert("L")).point(lambda v: 255 if v > 20 else 0).getbbox()
mark = fav.crop(bbox)
side = int(max(mark.size) * 1.08)
square = Image.new("RGB", (side, side), "white")
square.paste(mark, ((side - mark.width) // 2, (side - mark.height) // 2))
square_a = white_to_alpha(square.resize((512, 512), Image.LANCZOS))
square_a.resize((32, 32), Image.LANCZOS).save(OUT / "favicon-32.png", optimize=True)
square_a.resize((192, 192), Image.LANCZOS).save(OUT / "favicon-192.png", optimize=True)
square.resize((180, 180), Image.LANCZOS).save(OUT / "apple-touch-icon.png", optimize=True)
square_a.save(OUT.parent.parent / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

# Hero background (compressed, WebP + JPEG fallback).
hero = Image.open(SRC / "laptop_on_a_table.jpg").convert("RGB")
save_pair(hero, "hero", jpg_q=68, webp_q=66)

# Social sharing image 1200x630.
og = ImageOps.fit(hero, (1200, 630), Image.LANCZOS, centering=(0.5, 0.45))
og.save(OUT / "og-image.jpg", "JPEG", quality=78, optimize=True, progressive=True)

# Portrait, 4:5.
pic = Image.open(SRC / "ThomasPic01.jpg").convert("RGB")
pic = ImageOps.fit(pic, (640, 800), Image.LANCZOS, centering=(0.5, 0.35))
save_pair(pic, "thomas-moor", jpg_q=78, webp_q=76)

for f in sorted(OUT.iterdir()):
    print(f"{f.name:24} {f.stat().st_size / 1024:7.1f} KB")
