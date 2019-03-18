#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pypi_oldest_requirements` package."""
import os
import pickle
import sys
import pytest

from pypi_oldest_requirements import req_parse


def test_command_line_interface():
    """Test the CLI."""
    this_dir = os.path.dirname(os.path.abspath(__file__))
    req_file = os.path.join(this_dir, 'requirements.txt')
    pckl = os.path.join(this_dir, 'result.pickle')
    res = {(n, str(o)) for n, o in req_parse.get_oldest_from_req_file(req_file)}
    pickle.dump(res, open(pckl+'.new', 'wb'))
    assert res == pickle.load(open(pckl, 'rb'))


if __name__ == '__main__':
    sys.exit(pytest.main(sys.argv[1:] + [__file__, '-s']))
