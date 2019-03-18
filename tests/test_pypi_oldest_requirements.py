#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pypi_oldest_requirements` package."""
import os
import pickle
import pprint
import sys
import pytest

from pypi_oldest_requirements import requirements


def test_command_line_interface():
    """Test the CLI."""
    this_dir = os.path.dirname(os.path.abspath(__file__))
    req_file = os.path.join(this_dir, 'requirements.txt')
    pckl = os.path.join(this_dir, 'result.pickle')
    res = [(n, o) for n, o in requirements.get_oldest_from_req_file(req_file)]
    pprint.pprint(res)
    pickle.dump(res, open(pckl, 'wb'))


if __name__ == '__main__':
    sys.exit(pytest.main(sys.argv[1:] + [__file__, '-s']))
