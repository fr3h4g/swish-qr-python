from swish_qr.swish_qr import fix_amount


def test_fix_amount():
    assert fix_amount(0) == "0,00"
    assert fix_amount(0.123) == "0,12"
    assert fix_amount(0.129) == "0,13"
