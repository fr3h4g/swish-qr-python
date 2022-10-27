# Swish QR Code

<p>
<a href="https://github.com/fr3h4g/swish-qr-python/actions?query=event%3Apush+branch%3Amain" target="_blank">
    <img src="https://github.com/fr3h4g/swish-qr-python/actions/workflows/tests.yml/badge.svg" alt="Test"/>
</a>
<a href="https://codecov.io/gh/fr3h4g/swish-qr-python" > 
 <img src="https://codecov.io/gh/fr3h4g/swish-qr-python/branch/main/graph/badge.svg?token=8XP0FYQ0P0&" alt="Codecov"/> 
 </a>
 <a href="https://pypi.org/project/swish_qr" target="_blank">
    <img src="https://img.shields.io/pypi/v/swish_qr?color=%2334D058&label=pypi%20package" alt="Package version"/>
</a>
<a href="https://pypi.org/project/swish_qr" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/swish_qr.svg?color=%2334D058" alt="Supported Python versions"/>
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
