from click.testing import CliRunner

from swish_qr.cli import main

runner = CliRunner()


def test_cli_ok():
    response = runner.invoke(main, ["1234567890", "1", "1", "test.png"])
    assert response.exit_code == 0


def test_cli_payee_error():
    response = runner.invoke(main, ["123456789", "1", "1", "test.png"])
    assert response.exit_code == 2
    response = runner.invoke(main, ["12345678901", "1", "1", "test.png"])
    assert response.exit_code == 2
    response = runner.invoke(main, ["ABCDEFGHIJK", "1", "1", "test.png"])
    assert response.exit_code == 2


def test_cli_amount_error():
    response = runner.invoke(main, ["1234567890", "0", "1", "test.png"])
    assert response.exit_code == 2
    response = runner.invoke(main, ["1234567890", "150001", "1", "test.png"])
    assert response.exit_code == 2


def test_cli_message_error():
    response = runner.invoke(
        main,
        [
            "1234567890",
            "1",
            "123456789012345678901234567890123456789012345678901",
            "test.png",
        ],
    )
    assert response.exit_code == 2


def test_cli_filename_error():
    response = runner.invoke(
        main,
        [
            "1234567890",
            "1",
            "1",
        ],
    )
    assert response.exit_code == 2
    response = runner.invoke(
        main,
        ["1234567890", "1", "1", "////.png"],
    )
    assert response.exit_code == 2
