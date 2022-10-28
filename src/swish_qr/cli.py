import click
from swish_qr.swish_qr import generate_swish_code


@click.command()
@click.argument("payee", type=str)
@click.argument("amount", type=float)
@click.argument("message", type=str)
@click.argument("filename", type=str)
@click.option(
    "--format", type=str, default="png", help="image format, svg or png, default=png"
)
def main(payee: str, amount: float, message: str, filename: str, format: str):
    if not payee.isnumeric():
        print(f"Error: Invalid value for 'PAYEE': '{payee}' is not a valid number.")
        exit(2)
    if len(payee) != 10:
        print("Error: Wrong length of 'PAYEE,' must be 10 digits.")
        exit(2)
    if amount < 1 or amount > 150000:
        print("Error: Wrong value in 'AMOUNT', allowed between 1 and 150000.")
        exit(2)
    if len(message) > 50:
        print("Error: Wrong length of 'MESSAGE', max length 50 characters.")
        exit(2)
    try:
        image_data = generate_swish_code(payee, amount, message, format)
        with open(filename, "wb") as f:
            f.write(image_data)
    except:  # noqa: E722
        print("Error: Can't generate image.")
        exit(2)
