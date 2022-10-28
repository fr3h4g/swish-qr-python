from swish_qr import generate_swish_code
from swish_qr.png import make_swish_png
import pytest


def test_png():
    png_bytes = generate_swish_code(
        "0123456789",
        100.99,
        "Test message!",
        format="png",
    )
    with open("sample.png", "wb") as f:
        f.write(png_bytes)


def test_png_border():
    with pytest.raises(ValueError):
        make_swish_png(None, border=-1)
