# Swish QR Code

<p>
<a href="https://github.com/fr3h4g/swish-qr-python/actions?query=event%3Apush+branch%3Amain" target="_blank">
    <img src="https://github.com/fr3h4g/swish-qr-python/actions/workflows/tests.yml/badge.svg" alt="Test">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/swish_qr.svg" alt="Supported Python versions">
</a>
</p>
Generate [Swish](https://www.swish.nu) styled QR Code as SVG or PNG image.

![Example](https://raw.githubusercontent.com/fr3h4g/swish-qr-python/main/example.png "Example")

## Installation

```
pip install swish_qr
```

## Usage

```python
from swish_qr import generate_swish_code

# save to svg
svg_bytes = generate_swish_code("0123456789", 100.99, "Test message!", format="svg")
with open("example.svg", "wb") as f:
    f.write(svg_bytes)

# save to png
png_bytes = generate_swish_code("0123456789", 100.99, "Test message!", format="png")
with open("example.png", "wb") as f:
    f.write(png_bytes)

```
