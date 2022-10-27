from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="swish_qr",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description="Swish QR Code Python Library",
    long_description=long_description,
    url="https://github.com/fr3h4g/swish-qr-python",
    author="Fredrik Haglund",
    author_email="fr3h4g@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=["numpy>=1.23.4"],
    zip_safe=False,
)
