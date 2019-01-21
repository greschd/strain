#!/usr/bin/env python
# -*- coding: utf-8 -*-

# © 2017-2019, ETH Zurich, Institut für Theoretische Physik
# Author: Dominik Gresch <greschd@gmx.ch>

import re

from setuptools import setup, find_packages

README = """Implementation of strains for III-V materials."""

with open('./strain/__init__.py', 'r') as f:
    MATCH_EXPR = "__version__[^'\"]+(['\"])([^'\"]+)"
    VERSION = re.search(MATCH_EXPR, f.read()).group(2).strip()

EXTRAS_REQUIRE = {
    'test': ['pytest'],
    'doc': [
        'sphinx',
        'sphinx-rtd-theme<0.3',
        'ipython>=6.2',
    ],
    'pre-commit': [
        'pre-commit',
        'yapf==0.21.0',
        'prospector',
    ]
}
EXTRAS_REQUIRE['dev'] = (
    EXTRAS_REQUIRE['pre-commit'] + EXTRAS_REQUIRE['doc'] +
    EXTRAS_REQUIRE['test']
)

setup(
    name='strain',
    version=VERSION,
    author='Dominik Gresch',
    url='http://z2pack.ethz.ch/strain',
    author_email='greschd@gmx.ch',
    install_requires=[
        'numpy', 'pymatgen<2019;python_version<"3"',
        'pymatgen;python_version>="3"', 'fsc.export'
    ],
    extras_require=EXTRAS_REQUIRE,
    description=README,
    long_description=README,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English', 'Operating System :: Unix',
        'Development Status :: 3 - Alpha', 'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    license='Apache 2.0',
    packages=find_packages()
)
