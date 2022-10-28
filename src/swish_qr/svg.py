from swish_qr.qrcodegen import QrCode
from swish_qr.svg_templates import (
    generate_corners,
    generate_logo,
    generate_svg_template,
)
from typing import List
import re
from swish_qr.clear_qr_data import clearCorner, clearSquare


def make_swish_svg(qr: QrCode, border: int) -> bytes:
    if border < 0:
        raise ValueError("Border must be non-negative")
    parts: List[str] = []

    size = qr.get_size()

    dot_size = 30
    dot_space = 3
    image_size = size * dot_size + (size * dot_space)

    BACKGROUND = ""  # '<rect width="100%" height="100%" fill="white"/>'
    DIMENSIONS = f' width="{image_size}" height="{image_size}"'
    margin = border
    VIEWBOX = f"{4-margin} {4-margin} {(size + (margin * 2))} {(size + (margin * 2))}"
    CORNERS = generate_corners(size)

    LOGO = generate_logo(size, margin)

    centerSide = round(((0.2 * size) + 3.4) / 2) * 2 - 1
    center = round((size - centerSide) / 2)

    clearSquare(qr._modules, 0, 0, 7)
    clearSquare(qr._modules, size - 7, 0, 7)
    clearSquare(qr._modules, 0, size - 7, 7)
    clearSquare(qr._modules, center, center, centerSide)
    clearCorner(qr._modules, size)

    for y in range(qr.get_size()):
        for x in range(qr.get_size()):
            if qr.get_module(x, y):
                parts.append(
                    f'<circle cx="{x+margin+4}.5" cy="{y+margin+4}.5" r="0.46"/>'
                )

    CIRCLES = "".join(parts)
    svg = generate_svg_template(VIEWBOX, DIMENSIONS, BACKGROUND, CIRCLES, CORNERS, LOGO)
    svg = svg.replace("\n", "")
    svg = re.sub(r">\s*<", "><", svg)
    svg = svg.encode("utf8")

    return svg
