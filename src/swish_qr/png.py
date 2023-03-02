import numpy
import io
from PIL import Image, ImageDraw
from swish_qr.qrcodegen import QrCode
from swish_qr.clear_qr_data import clearCorner, clearSquare


def generate_corner():
    from PIL import Image, ImageDraw

    # im = Image.open("swish-corner.png")

    im = Image.new(
        "RGBA",
        (228, 228),
    )
    draw = ImageDraw.Draw(im)

    color = (255, 255, 255)

    # middle part
    draw.arc([(65, 68), (260, 265)], start=180, end=270, fill=color, width=100)

    # big arc
    draw.arc([(0, 0), (366, 366)], start=180, end=270, fill=color, width=32)

    # corner 1
    x, y, size = 0, 197, 30
    draw.arc([(x, y), (x + size, y + size)], start=90, end=180, fill=color, width=16)

    # corner 2
    x, y, size = 197, 197, 30
    draw.arc([(x, y), (x + size, y + size)], start=0, end=90, fill=color, width=16)

    # corner 3
    x, y, size = 197, 0, 30
    draw.arc([(x, y), (x + size, y + size)], start=270, end=0, fill=color, width=16)

    draw.line([(16, 211), (211, 211)], fill=color, width=32)
    draw.line([(211, 16), (211, 211)], fill=color, width=32)

    draw.line([(15, 183), (15, 211)], fill=color, width=32)
    draw.line([(183, 15), (211, 15)], fill=color, width=32)

    return im


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


def make_swish_png(qr: QrCode, border: int) -> bytes:
    if border < 0:
        raise ValueError("Border must be non-negative")
    size = qr.get_size()

    dot_size = 30
    dot_space = 3
    image_size = size * dot_size + (size * dot_space)
    corner_size = 7 * dot_size + (7 * dot_space)

    w, h = image_size, image_size

    image = generate_swish_gradient().resize((w, h))
    logo_size = round(6 * (size + 8))
    logo = Image.open("swish-logo.png").resize(
        (
            logo_size,
            logo_size,
        )
    )
    corner1 = generate_corner().resize((corner_size, corner_size))
    corner2 = generate_corner().rotate(90).resize((corner_size, corner_size))
    corner3 = generate_corner().rotate(270).resize((corner_size, corner_size))
    alpha = Image.new("L", (w, h))
    draw = ImageDraw.Draw(alpha)

    corner_pos = (size - 7) * dot_size + ((size - 7) * dot_space)

    Image.Image.paste(alpha, corner1)
    Image.Image.paste(alpha, corner2, (0, corner_pos))
    Image.Image.paste(alpha, corner3, (corner_pos, 0))

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
    # logo_pos = (center + 0.5) * dot_size + ((center + 0.5) * dot_space)
    logo_pos = (image_size / 2) - (logo.width / 2)
    Image.Image.paste(image, logo, (round(logo_pos), round(logo_pos)))

    with io.BytesIO() as output:
        image.save(output, format="png")
        contents = output.getvalue()
        return contents
