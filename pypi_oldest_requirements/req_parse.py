from pkg_resources import parse_requirements
from requirements import parser
from packaging.specifiers import SpecifierSet

from pypi_oldest_requirements import pypi

def get_oldest_version(req):
    available_versions = pypi.get_versions(req.name)
    # actually a packaging.specifiers.SpecifierSet
    if isinstance(req.specifier, SpecifierSet):
        spec_set = req.specifier
    else:
        spec_set = SpecifierSet(specifiers=','.join((''.join(s) for s in req.specs)))

    for av in sorted(available_versions, reverse=False):
        # for some reason 'av' is incompatible 'Version" object that spec_set wants to parse again
        if spec_set.contains(str(av)):
            return av
    raise RuntimeError(f'no matching version for {req.project_name}')


def get_oldest_from_req_file(req_file):
    parsed = []
    for line in open(req_file, 'rt').readlines():
        try:
            gen = list(parse_requirements(line))
        except :
            gen = list(parser.parse(line))
        for req in gen:
            parsed.append(req)
    for req in parsed:
        yield req.name, get_oldest_version(req)
