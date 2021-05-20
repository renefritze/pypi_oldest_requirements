#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pypi_oldest_requirements` package."""
import re
import sys
import pytest

from pypi_oldest_requirements import req_parse
from pypi_oldest_requirements.cli import transform

REQUIREMENT_FILES = [
    ["small.txt"],
    ["small-optional.txt"],
    ["small.txt", "small-optional.txt"],
    ["requirements-ci.txt"],
    ["requirements-optional.txt"],
    ["requirements-docker-other.txt"],
    ["requirements.txt"],
    [
        "requirements-ci.txt",
        "requirements-optional.txt",
        "requirements-docker-other.txt",
        "requirements.txt",
    ],
]

EXT = f"py_{sys.version_info[0]}_{sys.version_info[1]}_"


@pytest.fixture(
    params=REQUIREMENT_FILES,
    ids=[
        "__".join(
            (
                f.replace(
                    ".txt",
                    "",
                )
                for f in fns
            )
        )
        for fns in REQUIREMENT_FILES
    ],
)
def requirement_files(request, shared_datadir):
    fn = [shared_datadir / p for p in request.param]
    assert all(f.exists() for f in fn)
    basename = re.sub(r"[\W]", "_", request.node.name)
    return fn, f"{basename}_{EXT}"


def test_oldest_req(requirement_files, data_regression):
    requirement_files, basename = requirement_files
    res = {
        (n, str(o)) for n, o in req_parse.get_oldest_from_req_file(requirement_files)
    }
    data_regression.check(res, basename=basename)


def test_minimal_req(requirement_files, file_regression):
    requirement_files, basename = requirement_files
    res = "".join(req_parse.get_minimal_restricted_from_req_file(requirement_files))
    file_regression.check(res, basename=basename)


def test_cli_transform(requirement_files, file_regression, tmpdir):
    requirement_files, basename = requirement_files
    tmp_path = tmpdir / "transform.txt"
    transform(requirement_files, output_fn=tmp_path)
    file_regression.check(open(tmp_path, "rt").read(), basename=basename)


if __name__ == "__main__":
    sys.exit(pytest.main(sys.argv[1:] + [__file__, "-s"]))
