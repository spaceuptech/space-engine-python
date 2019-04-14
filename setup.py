# https://realpython.com/pypi-publish-python-package
import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="space_engine",
    version="1.0.0",
    description="SpaceUp API for Space Cloud FaaS Engines",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/spaceuptech/space-engine-python",
    author="SpaceUp Tech",
    author_email="info@spaceuptech.com",
    license="Apache License, Version 2.0",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["space_engine"],
    include_package_data=True,
    install_requires=["nats-python"]
)