#!/usr/bin/env python3

# Copyright 2023 Facundo Batista
# Licensed under the GPL v3 License
# For further info, check https://github.com/facundobatista/runish

"""Setup script for Runish."""

from setuptools import setup


VERSION = "0.1"


setup(
    name="runish",
    version=VERSION,
    author="Facundo Batista",
    author_email="facundo@taniquetil.com.ar",
    description="A Unicode name finder and characters explainer.",
    long_description=open("README.rst", "rt", encoding="utf8").read(),
    url="https://github.com/facundobatista/runish",
    license="GPL-v3",
    packages=["runish"],
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts": ["runish = runish.runish:main"],
    },
    install_requires=[],
    python_requires=">=3",
)
