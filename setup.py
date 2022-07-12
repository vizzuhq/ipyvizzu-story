#!/usr/bin/env python3
from setuptools import setup, find_packages

with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

with open("README.md") as fp:
    long_description = fp.read()

setup(
    name="ipyvizzu-story",
    version="0.0.0",
    description="A presentation extension for ipyvizzu to create presentations with animated data visualisations with ease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2",
    packages=find_packages(where="src", exclude=["__pycache__"]),
    package_dir={"": "src"},
    package_data={"ipyvizzustory": ["py.typed"]},
    python_requires=">=3.6",
    install_requires=requirements,
    url="https://github.com/vizzuhq/ipyvizzu-story",
    project_urls={
        "Documentation": "https://github.com/vizzuhq/ipyvizzu-story",
        "Source": "https://github.com/vizzuhq/ipyvizzu-story",
        "Tracker": "https://github.com/vizzuhq/ipyvizzu-story/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
)
