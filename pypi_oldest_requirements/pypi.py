# -*- coding: utf-8 -*-

"""Main module."""
import ssl
import requests
from packaging import version
from requests_toolbelt import SSLAdapter


def get_versions(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    s = requests.Session()
    s.mount('https://', SSLAdapter(ssl.PROTOCOL_TLSv1_2))
    r = s.get(url)
    try:
        versions = [version.parse(k) for k in r.json()['releases'].keys()]
    except KeyError:
        return []
    return versions
