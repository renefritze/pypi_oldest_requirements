# -*- coding: utf-8 -*-

"""Console script for pypi_oldest_requirements."""
import sys
from pathlib import Path
from typing import List

import typer


def main(requirements_files: List[str]):
    for req in requirements_files:
        path = Path(req).resolve()
        if not path.exists():
            print(f"File {req} does not exist. Aborting")
            sys.exit(-1)
        _main(req)


def _main(requirements_file):
    from pypi_oldest_requirements import req_parse, req_write

    oldest = list(req_parse.get_oldest_from_req_file(requirements_file))
    req_write.write_exact_pinned_requirements(requirements_file + ".oldest", oldest)

    skip = 1
    major = list(req_parse.get_last_majors_from_req_file(requirements_file, skip))
    req_write.write_exact_pinned_requirements(requirements_file + ".major", major)

    minimal = list(req_parse.get_minimal_restricted_from_req_file(requirements_file))
    req_write.write_requirements(requirements_file + ".minimal", minimal)


def transform(filenames: List[str], output_fn: str = None):
    output_fn = output_fn or filenames[0] + ".minimal"
    filenames = [Path(fn).resolve() for fn in filenames]
    assert all((fn.exists() for fn in filenames))
    from pypi_oldest_requirements import req_parse, req_write

    minimal = list(req_parse.get_minimal_restricted_from_req_file(filenames))
    req_write.write_requirements(output_fn, minimal)


def run():
    typer.run(transform)
