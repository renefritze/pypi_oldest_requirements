# -*- coding: utf-8 -*-

"""Main module."""
import ssl

import packaging
import requests
from packaging import version
from requests_toolbelt import SSLAdapter


def get_versions(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    s = requests.Session()
    s.mount("https://", SSLAdapter(ssl.PROTOCOL_TLSv1_2))
    r = s.get(url)
    try:
        keys = r.json()["releases"].keys()
        versions = []
        for k in keys:
            try:
                versions.append(version.parse(k))
            except packaging.version.InvalidVersion:
                pass
    except KeyError:
        return []
    return versions
