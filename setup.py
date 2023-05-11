"""
ipyvizzu-story
Build, present and share animated data stories in Jupyter Notebook and similar environments.
"""

from setuptools import setup, find_packages  # type: ignore


with open("requirements.txt", encoding="utf8") as fp:
    requirements = fp.read().splitlines()

with open("README.md", encoding="utf8") as fp:
    long_description = fp.read()

packages = find_packages(where="src", exclude=["__pycache__"])

setup(
    name="ipyvizzu-story",
    version="0.7.0",
    description=(
        "Build, present and share animated data stories in Jupyter Notebook and similar environments."  # pylint: disable=line-too-long
    ),
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
        "panel": ["panel"],
    },
    url="https://github.com/vizzuhq/ipyvizzu-story",
    project_urls={
        "Documentation": "https://ipyvizzu-story.vizzuhq.com",
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
