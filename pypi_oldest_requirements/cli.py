# -*- coding: utf-8 -*-

"""Console script for pypi_oldest_requirements."""
import sys


def main(requirements_file):
    from pypi_oldest_requirements import requirements
    for name, oldest in requirements.get_oldest_from_req_file(requirements_file):
        print(f'{name}: {oldest}')


if __name__ == "__main__":
    main(sys.argv[1])

