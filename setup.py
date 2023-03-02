import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

REQUIRES = [
    "httpx >= 0.15.0, < 0.24.0",
    "attrs >= 21.3.0",
    "python-dateutil >= 2.8.0, < 3",
    "boto3~=1.24.78",
    "requests==2.25",
    "frozendict==2.3.4",
    "pandas==1.5.2",
]

setup(
    name="priceloop-api",
    version="0.77.1",
    description="A client library for accessing Priceloop API",
    author="Priceloop",
    author_email="hello@priceloop.ai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/priceloop/priceloop-api-python",
    packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=REQUIRES,
    package_data={"priceloop_api": ["py.typed"]},
)
