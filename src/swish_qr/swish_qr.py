from swish_qr.qrcodegen import QrCode
from swish_qr.svg import make_swish_svg
from swish_qr.png import make_swish_png


def fix_amount(amount):
    amount_str = "{:.2f}".format(amount).replace(".", ",")
    return amount_str


def generate_swish_code(
    payee: str,
    amount: float,
    message: str,
    format: str = "png",
    edit_amount=False,
    edit_message=False,
) -> bytes:
    if (
        not isinstance(format, str)
        or not format
        or format.lower() not in ["svg", "png"]
    ):
        raise ValueError("unknown format")
    if len(str(payee)) != 10:
        raise ValueError("payee too long, max 10 characters")
    if not message:
        message = ""
    if len(str(message)) > 50:
        raise ValueError("message too long, max 50 characters")

    amount_str = fix_amount(amount)

    edit_mask = 0
    if edit_amount:
        edit_mask += 4
    if edit_message:
        edit_mask += 2

    text = f"C{payee};{amount_str};{message};{edit_mask}"
    qr_code = QrCode.encode_text(
        text,
        QrCode.Ecc.MEDIUM,
    )

    if format.lower() == "svg":
        svg = make_swish_svg(qr_code, 0)
        return svg
    else:
        png = make_swish_png(qr_code, 0)
        return png
