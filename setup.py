#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import sys
import os

sys.path.append(os.path.dirname(__file__))
import versioneer

requirements = [
    "packaging",
    "requirements-parser",
    "requests",
    "requests-toolbelt",
    "typer",
    "click<8",
]

setup_requirements = [
    "pytest-runner",
]

test_requirements = ["pytest", "pytest-cov", "tox", "twine"]

setup(
    author="René Fritze",
    author_email="rene.fritze@wwu.de",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description='Get "oldest" fitting requirements from pypi',
    entry_points={
        "console_scripts": [
            "pypi_minimal_requirements_pinned=pypi_oldest_requirements.cli:run",
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="pypi_oldest_requirements",
    name="pypi_oldest_requirements",
    packages=find_packages(include=["pypi_oldest_requirements"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/renefritze/pypi_oldest_requirements",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False,
    python_requires=">=3.6",
)
