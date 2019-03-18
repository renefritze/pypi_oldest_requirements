from . import pypi

from pkg_resources import parse_requirements


def get_oldest_version(req):
    available_versions = pypi.get_versions(req.name)
    # actually a packaging.specifiers.SpecifierSet
    spec_set = req.specifier
    for av in sorted(available_versions, reverse=False):
        # for some reason 'av' is incompatible 'Version" object that spec_set wants to parse again
        if spec_set.contains(str(av)):
            return av
    raise RuntimeError(f'no matching version for {req.project_name}')


def get_oldest_from_req_file(req_file):
    parsed = parse_requirements(open(req_file, 'rt').readlines())
    for req in parsed:
        yield req.name, get_oldest_version(req)
