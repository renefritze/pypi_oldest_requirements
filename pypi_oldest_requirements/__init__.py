# -*- coding: utf-8 -*-

"""Top-level package for PyPi Oldest Requirements."""

__author__ = """René Fritze"""
__email__ = "rene.fritze@wwu.de"

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pypi_oldest_requirements")
except PackageNotFoundError:
    __version__ = "unknown version"
