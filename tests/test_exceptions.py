from swish_qr import generate_swish_code
import pytest


def test_format_exception():
    with pytest.raises(ValueError):
        generate_swish_code(
            "0123456789",
            100.99,
            "Test message!",
            format="bmp",
        )
    with pytest.raises(ValueError):
        generate_swish_code(
            "0123456789",
            100.99,
            "Test message!",
            format=None,
        )
    with pytest.raises(ValueError):
        generate_swish_code(
            "0123456789",
            100.99,
            "Test message!",
            format=1,
        )


def test_payee_exception():
    with pytest.raises(ValueError):
        generate_swish_code(
            "012345678",
            100.99,
            "Test message!",
            format="png",
        )
    with pytest.raises(ValueError):
        generate_swish_code(
            "01234567891",
            100.99,
            "Test message!",
            format="png",
        )
    with pytest.raises(ValueError):
        generate_swish_code(
            "",
            100.99,
            "Test message!",
            format="png",
        )
    with pytest.raises(ValueError):
        generate_swish_code(
            None,
            100.99,
            "Test message!",
            format="png",
        )
    with pytest.raises(ValueError):
        generate_swish_code(
            1,
            100.99,
            "Test message!",
            format="png",
        )


def test_message_exception():
    with pytest.raises(ValueError):
        generate_swish_code(
            "0123456789",
            100.99,
            "123456789012345678901234567890123456789012345678901",
            format="png",
        )
