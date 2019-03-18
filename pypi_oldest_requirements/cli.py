# -*- coding: utf-8 -*-

"""Console script for pypi_oldest_requirements."""
import sys


def main(requirements_file):
    from pypi_oldest_requirements import req_parse
    for name, oldest in req_parse.get_oldest_from_req_file(requirements_file):
        print(f'{name}: {oldest}')


if __name__ == "__main__":
    main(sys.argv[1])

