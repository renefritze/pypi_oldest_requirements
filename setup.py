#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['packaging']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', 'pytest-cov', 'tox', 'twine']

setup(
    author="René Fritze",
    author_email='rene.fritze@wwu.de',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description='Get "oldest" fitting requirements from pypi',
    entry_points={
        'console_scripts': [
            'pypi_oldest_requirements=pypi_oldest_requirements.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pypi_oldest_requirements',
    name='pypi_oldest_requirements',
    packages=find_packages(include=['pypi_oldest_requirements']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/renefritze/pypi_oldest_requirements',
    version='2019.0',
    zip_safe=False,
)
