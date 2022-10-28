import numpy
import io
from PIL import Image, ImageDraw
from swish_qr.qrcodegen import QrCode
from swish_qr.clear_qr_data import clearCorner, clearSquare


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
    logo_pos = (center + 1) * dot_size + ((center + 1) * dot_space)
    Image.Image.paste(image, logo, (logo_pos, logo_pos))

    with io.BytesIO() as output:
        image.save(output, format="png")
        contents = output.getvalue()
        return contents
