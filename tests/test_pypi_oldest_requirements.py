#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pypi_oldest_requirements` package."""
import sys
import pytest

from pypi_oldest_requirements import req_parse


@pytest.fixture(params=['requirements.txt', 'requirements-optional.txt'])
def requirement_file(request, shared_datadir):
    fn = shared_datadir / request.param
    assert fn.exists()
    return fn


def test_oldest_req(requirement_file, data_regression):
    res = {(n, str(o)) for n, o in req_parse.get_oldest_from_req_file(requirement_file)}
    data_regression.check(res)


def test_minimal_req(requirement_file, file_regression):
    res = ''.join(req_parse.get_minimal_restricted_from_req_file(requirement_file))
    file_regression.check(res)


if __name__ == '__main__':
    sys.exit(pytest.main(sys.argv[1:] + [__file__, '-s']))
