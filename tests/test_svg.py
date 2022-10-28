from swish_qr import generate_swish_code
from swish_qr.svg import make_swish_svg
import pytest


def test_svg():
    svg_bytes = generate_swish_code(
        "0123456789",
        100.99,
        "Test message!",
        format="svg",
    )
    with open("sample.svg", "wb") as f:
        f.write(svg_bytes)


def test_png_border():
    with pytest.raises(ValueError):
        make_swish_svg(None, border=-1)
