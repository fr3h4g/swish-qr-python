from swish_qr import generate_swish_code


def test_none_message():
    png_data = generate_swish_code("1234567890", 1, None)
    with open("test.png", "wb") as f:
        f.write(png_data)


def test_amount_not_locked():
    png_data = generate_swish_code("1234567890", 1, "Test", edit_amount=True)
    with open("test.png", "wb") as f:
        f.write(png_data)


def test_message_not_locked():
    png_data = generate_swish_code("1234567890", 1, "Test", edit_message=True)
    with open("test.png", "wb") as f:
        f.write(png_data)
