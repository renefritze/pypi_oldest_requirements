# -*- coding: utf-8 -*-

"""Console script for pypi_oldest_requirements."""
import pprint
import sys


def main(requirements_file):
    from pypi_oldest_requirements import req_parse, req_write
    oldest = list(req_parse.get_oldest_from_req_file(requirements_file))
    req_write.write_exact_pinned_requirements(requirements_file + '.oldest', oldest)

    skip = 1
    major = list(req_parse.get_last_majors_from_req_file(requirements_file, skip))
    req_write.write_exact_pinned_requirements(requirements_file + '.major', oldest)

    minimal = list(req_parse.get_minimal_restricted_from_req_file(requirements_file))
    req_write.write_requirements(requirements_file + '.minimal', minimal)


if __name__ == "__main__":
    main(sys.argv[1])

