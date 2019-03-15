# -*- coding: utf-8 -*-

"""Main module."""

import requests


def get_versions(package_name):
    r = requests.get(f"https://pypi.org/pypi/{package_name}/json")
    try:
        versions = r.json()['releases'].keys()
    except KeyError:
        return []
    return versions
