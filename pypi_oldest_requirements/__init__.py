# -*- coding: utf-8 -*-

"""Top-level package for PyPi Oldest Requirements."""

__author__ = """René Fritze"""
__email__ = "rene.fritze@wwu.de"
__version__ = "2020.4.2"

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
