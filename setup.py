#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="voice_recorder",
    version="1.0.0",
    author="E.P.W. Bernhard",
    author_email="manu.p.bernhard@gmail.com",
    description="Just a simple voice recorder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/epbernhard/voice_recorder",
    install_requires=['time', 'sounddevice', 'tqdm'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)