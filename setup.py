from setuptools import setup, find_packages

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="UTF-8") as fh:
    requirements = fh.read().split("\n")
setup(
    name="OpenScrape",
    version="0.0.1",
    packages=find_packages(),
    author="YUMA OBATA",
    author_email="yuma@umaxiaotian.com",
    description="OpenScrape is a powerful application that integrates with various services to scrape information. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/umaxiaotian/OpenScrape",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: AsyncIO",
    ],
    install_requires=[requirements],
)
