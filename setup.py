"""
ipyvizzu-story
Create and present animated data stories within data science notebooks.
"""

from setuptools import setup, find_packages  # type: ignore


with open("requirements.txt", encoding="utf8") as fp:
    requirements = fp.read().splitlines()

with open("README.md", encoding="utf8") as fp:
    long_description = fp.read()

packages = find_packages(where="src", exclude=["__pycache__"])

setup(
    name="ipyvizzu-story",
    version="0.2.1",
    description="Create and present animated data stories within data science notebooks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2",
    packages=packages,
    package_dir={"": "src"},
    package_data={package: ["py.typed"] for package in packages},
    python_requires=">=3.6",
    install_requires=requirements,
    extras_require={
        "jupyter": ["IPython"],
        "streamlit": ["streamlit"],
    },
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
