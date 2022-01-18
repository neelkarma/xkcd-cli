from setuptools import setup, find_packages

long_description = ""
with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="xkcd-cli-viewer",
    version="0.1.0",
    author="iamkneel",
    description="A CLI that scrapes the XKCD website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.github.com/neelkarma/xkcd-cli",
    packages=find_packages(where="src"),
    scripts=["bin/xkcd-cli"],
)
