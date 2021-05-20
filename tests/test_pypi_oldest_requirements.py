#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pypi_oldest_requirements` package."""
import sys
import pytest

from pypi_oldest_requirements import req_parse
from pypi_oldest_requirements.cli import transform


@pytest.fixture(
    params=[
        ["requirements.txt"],
        ["requirements-optional.txt"],
        ["requirements.txt", "requirements-optional.txt"],
    ]
)
def requirement_files(request, shared_datadir):
    fn = [shared_datadir / p for p in request.param]
    assert all(f.exists() for f in fn)
    return fn


def test_oldest_req(requirement_files, data_regression):
    res = {
        (n, str(o)) for n, o in req_parse.get_oldest_from_req_file(requirement_files)
    }
    data_regression.check(res)


def test_minimal_req(requirement_files, file_regression):
    res = "".join(req_parse.get_minimal_restricted_from_req_file(requirement_files))
    file_regression.check(res)


def test_cli_transform(requirement_files, file_regression, tmpdir):
    tmp_path = tmpdir / "transform.txt"
    transform(requirement_files, output_fn=tmp_path)
    file_regression.check(open(tmp_path, "rt").read())


if __name__ == "__main__":
    sys.exit(pytest.main(sys.argv[1:] + [__file__, "-s"]))
