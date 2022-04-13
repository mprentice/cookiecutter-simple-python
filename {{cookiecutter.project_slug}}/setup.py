"""Install with: `python setup.py install' or `pip install'"""
import io
import os
from glob import glob

from setuptools import find_packages, setup  # type: ignore


def read(*names, **kwargs):
    """Open and return text of file relative to this file's directory."""
    filename = os.path.join(os.path.dirname(__file__), *names)
    encoding = kwargs.get("encoding", "utf8")
    with io.open(filename, encoding=encoding) as filehandle:
        return filehandle.read()


INSTALL_REQUIRES = ["attrs"]
TEST_REQUIRES = INSTALL_REQUIRES + [
    "prospector",
    "mypy",
    "flake8",
    "flake8-black",
    "flake8-bugbear",
    "flake8-isort",
    "flake8-comprehensions",
    "flake8-docstrings",
    "pytest",
    "pytest-cov",
]
DEV_REQUIRES = TEST_REQUIRES + ["wheel", "importmagic", "epc", "jedi", "isort"]

setup(
    name="{{cookiecutter.project_slug}}",
    version="0.1.0",
    license="MIT License",
    description="{{cookiecutter.project_short_description}}",
    long_description=read("README.rst"),
    author="{{cookiecutter.author}}",
    email="{{cookiecutter.email}}",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[
        os.path.splitext(os.path.basename(path))[0] for path in glob("src/*.py")
    ],
    include_package_data=True,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    python_requires=">=3.7",
    install_requires=INSTALL_REQUIRES,
    extras_require={"dev": DEV_REQUIRES, "test": TEST_REQUIRES},
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}} = {{cookiecutter.project_slug}}.cli:main",
        ]
    },
)
