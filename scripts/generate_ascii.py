#!/usr/bin/env python3
"""Generate real ASCII text + SVG from a portrait.

This is an original implementation inspired by the image-to-ASCII pipeline used by
GitAscii: perceptual luminance, local contrast, edge preservation, and optional
Floyd-Steinberg error diffusion. It does not copy GitAscii source code.
"""
from __future__ import annotations

import argparse
import html
from pathlib import Path
from typing import Iterable

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

DENSE = "@%#*+=-:. "
# A denser ramp for facial detail. XML-sensitive characters are avoided on purpose.
DENSE_FINE = "@MWB8%#*oahkbdpqwmZO0QLCJUYXzcvunxrjft1ilI;:,.' `"


def center_crop_face(img: Image.Image) -> Image.Image:
    """Portrait crop tuned for the supplied photo: face, glasses, hand, shoulders."""
    w, h = img.size
    # Relative crop keeps this usable if the source is replaced by a similarly framed photo.
    left = int(w * 0.23)
    top = int(h * 0.10)
    right = int(w * 0.84)
    bottom = int(h * 0.82)
    return img.crop((left, top, right, bottom))


def perceptual_luminance(rgb: np.ndarray) -> np.ndarray:
    """Approximate sRGB luminance after linearization."""
    x = rgb.astype(np.float32) / 255.0
    linear = np.where(x <= 0.04045, x / 12.92, ((x + 0.055) / 1.055) ** 2.4)
    y = 0.2126 * linear[..., 0] + 0.7152 * linear[..., 1] + 0.0722 * linear[..., 2]
    # encode back into a display-like 0..255 luminance for easier tuning
    srgb_y = np.where(y <= 0.0031308, 12.92 * y, 1.055 * (y ** (1/2.4)) - 0.055)
    return np.clip(srgb_y * 255.0, 0, 255)


def floyd_steinberg(values: np.ndarray, levels: int = 16) -> np.ndarray:
    """Error-diffuse luminance before character mapping."""
    arr = values.astype(np.float32).copy()
    h, w = arr.shape
    step = 255.0 / max(1, levels - 1)
    for y in range(h):
        for x in range(w):
            old = arr[y, x]
            new = round(old / step) * step
            err = old - new
            arr[y, x] = new
            if x + 1 < w:
                arr[y, x + 1] += err * 7 / 16
            if y + 1 < h:
                if x > 0:
                    arr[y + 1, x - 1] += err * 3 / 16
                arr[y + 1, x] += err * 5 / 16
                if x + 1 < w:
                    arr[y + 1, x + 1] += err * 1 / 16
    return np.clip(arr, 0, 255)


def prepare_luminance(img: Image.Image, cols: int, contrast: float = 1.45, gamma: float = 1.02,
                      edge_strength: float = 0.22, dither: bool = True) -> np.ndarray:
    img = center_crop_face(img.convert("RGB"))

    # Suppress the strongly green outdoor background in the supplied portrait.
    # Pixels that are clearly vegetation-like are pushed to white so they become
    # spaces in the ASCII matrix, keeping attention on the face / glasses / hand.
    rgb0 = np.asarray(img).copy()
    r, g, b = rgb0[..., 0], rgb0[..., 1], rgb0[..., 2]
    green_bg = (g > r * 1.12) & (g > b * 1.10) & ((g.astype(int) - r.astype(int)) > 12)
    rgb0[green_bg] = [255, 255, 255]
    img = Image.fromarray(rgb0.astype(np.uint8), mode="RGB")

    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Sharpness(img).enhance(1.35)

    # Preserve important facial boundaries by blending a mild high-pass image.
    gray = ImageOps.grayscale(img)
    blurred = gray.filter(ImageFilter.GaussianBlur(radius=1.4))
    edge = ImageOps.autocontrast(Image.fromarray(np.abs(
        np.asarray(gray, dtype=np.int16) - np.asarray(blurred, dtype=np.int16)
    ).astype(np.uint8)))
    edge_arr = np.asarray(edge, dtype=np.float32)

    # Character cells are taller than wide, so compensate vertically.
    aspect = img.height / img.width
    rows = max(20, int(cols * aspect * 0.46))
    small = img.resize((cols, rows), Image.Resampling.LANCZOS)
    lum = perceptual_luminance(np.asarray(small))

    edge_small = edge.resize((cols, rows), Image.Resampling.LANCZOS)
    edge_small_arr = np.asarray(edge_small, dtype=np.float32)
    lum = lum - edge_strength * edge_small_arr

    # robust auto-contrast
    lo, hi = np.percentile(lum, [2, 98])
    lum = np.clip((lum - lo) * (255.0 / max(1.0, hi - lo)), 0, 255)
    lum = 255.0 * ((lum / 255.0) ** gamma)

    if dither:
        lum = floyd_steinberg(lum, levels=18)
    return lum


def to_ascii(lum: np.ndarray, charset: str = DENSE_FINE, invert: bool = False) -> list[str]:
    chars = charset if not invert else charset[::-1]
    n = len(chars) - 1
    rows = []
    for row in lum:
        line = "".join(chars[int((v / 255.0) * n)] for v in row)
        rows.append(line.rstrip())
    return rows


def render_svg(rows: Iterable[str], out: Path, fg: str = "#F0FFF0", bg: str = "#050807",
               font_size: int = 10, line_height: int = 11, padding: int = 20) -> None:
    rows = list(rows)
    max_cols = max((len(r) for r in rows), default=1)
    char_w = font_size * 0.61
    width = int(max_cols * char_w + padding * 2)
    height = int(len(rows) * line_height + padding * 2)
    text = []
    y = padding + font_size
    for i, row in enumerate(rows):
        # subtle top-to-bottom reveal; harmless if animation is disabled by a renderer
        delay = min(1.2, i * 0.012)
        text.append(
            f'<text x="{padding}" y="{y + i*line_height}" class="row" '
            f'style="animation-delay:{delay:.3f}s">{html.escape(row)}</text>'
        )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <rect width="100%" height="100%" rx="10" fill="{bg}"/>
  <style>
    .row {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      font-size: {font_size}px;
      fill: {fg};
      white-space: pre;
      opacity: 1;
    }}
    @keyframes reveal {{ to {{ opacity: 1; }} }}
    @media (prefers-reduced-motion: reduce) {{ .row {{ animation: none; opacity: 1; }} }}
  </style>
  {''.join(text)}
</svg>'''
    out.write_text(svg, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--cols", type=int, default=92)
    ap.add_argument("--txt", default="assets/ascii-portrait.txt")
    ap.add_argument("--svg", default="assets/ascii-portrait.svg")
    ap.add_argument("--no-dither", action="store_true")
    args = ap.parse_args()

    img = Image.open(args.image)
    lum = prepare_luminance(img, cols=args.cols, dither=not args.no_dither)
    rows = to_ascii(lum, charset=DENSE)
    Path(args.txt).write_text("\n".join(rows) + "\n", encoding="utf-8")
    render_svg(rows, Path(args.svg))


if __name__ == "__main__":
    main()
