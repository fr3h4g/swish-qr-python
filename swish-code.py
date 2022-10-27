from PIL import Image, ImageDraw

import numpy

from qrcodegen import *
from svg_templates import generate_corners, generate_logo, generate_svg_template


def clearSquare(data, size, x, y, side):
    for yOffset in range(0, side):
        for xOffset in range(0, side):
            data[x + xOffset][y + yOffset] = False


def clearCorner(data, size):
    for yOffset in range(size - 6, size):
        for xOffset in range(size - 1, size - 5, -1):
            if xOffset > size - 6 + (size - yOffset):
                data[xOffset][yOffset] = False


def make_swish_svg(qr: QrCode, border: int) -> str:
    if border < 0:
        raise ValueError("Border must be non-negative")
    parts: List[str] = []

    BACKGROUND = '<rect width="100%" height="100%" fill="white"/>'
    DIMENSIONS = ' width="1200" height="1200"'
    size = qr.get_size()
    margin = border
    VIEWBOX = f"0 0 {size+margin*2} {size+margin*2}"
    CORNERS = generate_corners(size)

    LOGO = generate_logo(size, margin)

    centerSide = round(((0.2 * size) + 3.4) / 2) * 2 - 1
    center = round((size - centerSide) / 2)

    clearSquare(qr._modules, size, 0, 0, 7)
    clearSquare(qr._modules, size, size - 7, 0, 7)
    clearSquare(qr._modules, size, 0, size - 7, 7)
    clearSquare(qr._modules, size, center, center, centerSide)
    clearCorner(qr._modules, size)

    for y in range(qr.get_size()):
        for x in range(qr.get_size()):
            if qr.get_module(x, y):
                parts.append(f'<circle cx="{x+margin}.5" cy="{y+margin}.5" r="0.46"/>')

    CIRCLES = "".join(parts)

    return generate_svg_template(
        VIEWBOX, DIMENSIONS, BACKGROUND, CIRCLES, CORNERS, LOGO
    )


def generate_swish_gradient():
    scale = 3
    color_a = [180, 47, 146]
    color_b = [239, 64, 35]
    size = round(4250 / scale)
    crop_from = round(620 / scale)
    crop_to = round(3620 / scale)
    croparea = (
        crop_from,
        crop_from,
        crop_to,
        crop_to,
    )
    gradient = numpy.zeros((size, size, 3), numpy.uint8)
    gradient[:, :, 0] = numpy.linspace(color_a[0], color_b[0], size, dtype=numpy.uint8)
    gradient[:, :, 1] = numpy.linspace(color_a[1], color_b[1], size, dtype=numpy.uint8)
    gradient[:, :, 2] = numpy.linspace(color_a[2], color_b[2], size, dtype=numpy.uint8)
    return Image.fromarray(gradient).rotate(45).crop(croparea)


def fix_amount(amount):
    amount_str = "{:.2f}".format(amount).replace(".", ",")
    return amount_str


def generate_swish_code(
    payee: str,
    amount: float,
    message: str,
    edit_amount=False,
    edit_payee=False,
):
    if len(str(payee)) > 10:
        raise ValueError("payee too long, max 10 characters")
    if len(message) > 50:
        raise ValueError("message too long, max 50 characters")
    amount_str = fix_amount(amount)
    edit_mask = 0
    if edit_amount:
        edit_mask += 4
    if edit_payee:
        edit_mask += 2
    text = f"C{payee};{amount_str};{message};{edit_mask}"
    print(text)
    qr0 = QrCode.encode_text(
        text,
        QrCode.Ecc.MEDIUM,
    )

    svg = make_swish_svg(qr0, 4)
    svg = svg.replace("\n", "")
    svg = re.sub(r">\s*<", "><", svg)
    with open("test.svg", "w") as f:
        f.write(svg)

    png = make_swish_png(qr0, 4)


def make_swish_png(qr: QrCode, border: int) -> str:
    size = qr.get_size()

    dot_size = 25
    dot_space = 3
    image_size = size * dot_size + (size * dot_space)
    corner_size = 7 * dot_size + (7 * dot_space)

    w, h = image_size, image_size

    image = generate_swish_gradient().resize((w, h))
    logo = Image.open("swish-logo.png").resize((corner_size, corner_size))
    corner1 = Image.open("swish-corner.png").resize((corner_size, corner_size))
    corner2 = (
        Image.open("swish-corner.png").rotate(90).resize((corner_size, corner_size))
    )
    corner3 = (
        Image.open("swish-corner.png").rotate(270).resize((corner_size, corner_size))
    )
    alpha = Image.new("L", (w, h))
    draw = ImageDraw.Draw(alpha)

    corner_pos = (size - 7) * dot_size + ((size - 7) * dot_space)

    Image.Image.paste(alpha, corner1)
    Image.Image.paste(alpha, corner2, (0, corner_pos))
    Image.Image.paste(alpha, corner3, (corner_pos, 0))

    centerSide = round(((0.2 * size) + 3.4) / 2) * 2 - 1
    center = round((size - centerSide) / 2)

    clearSquare(qr._modules, size, 0, 0, 7)
    clearSquare(qr._modules, size, size - 7, 0, 7)
    clearSquare(qr._modules, size, 0, size - 7, 7)
    clearSquare(qr._modules, size, center, center, centerSide)
    clearCorner(qr._modules, size)

    for y in range(qr.get_size()):
        for x in range(qr.get_size()):
            if qr.get_module(x, y):
                draw.ellipse(
                    (
                        x * dot_size + (x * dot_space),
                        y * dot_size + (y * dot_space),
                        x * dot_size + (x * dot_space) + dot_size,
                        y * dot_size + (y * dot_space) + dot_size,
                    ),
                    fill="white",
                    outline="white",
                )

    image.putalpha(alpha)
    logo_pos = (center + 1) * dot_size + ((center + 1) * dot_space)
    Image.Image.paste(image, logo, (logo_pos, logo_pos))
    image.save("test.png")


if __name__ == "__main__":
    generate_swish_code(
        "0739316106", 1, "12345678901234567890123456789012345678901234567890"
    )
