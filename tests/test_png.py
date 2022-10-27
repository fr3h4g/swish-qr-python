from swish_qr import generate_swish_code


def test_png():
    png_bytes = generate_swish_code(
        "0123456789",
        100.99,
        "Test message!",
        format="png",
    )
    with open("sample.png", "wb") as f:
        f.write(png_bytes)
