import os

from setuptools import setup, find_packages


def parse_requirements(filename):
    """load requirements from a pip requirements file"""
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


install_reqs = parse_requirements("requirements.txt")
version = "1.2.13"


description = "xpath/css based scraper with pagination"
long_description = description

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name="hodorlive",
    version=version,
    packages=find_packages(),
    install_requires=install_reqs,
    include_package_data=True,
    license="MIT",
    description=description,
    long_description=long_description,
    keywords=["hodor", "cssselect", "lxml", "scraping"],
    url="https://github.com/CompileInc/hodor",
    download_url="https://github.com/CompileInc/hodor/archive/v{version}.tar.gz".format(
        version=version
    ),
    author="Compile Inc",
    author_email="dev@compile.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
    ],
)
