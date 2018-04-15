#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from setuptools import setup, find_packages

readme = """Implementation of strains for III-V materials."""

with open('./strain/_version.py', 'r') as f:
    match_expr = "__version__[^'\"]+(['\"])([^'\"]+)"
    version = re.search(match_expr, f.read()).group(2).strip()

setup(
    name='strain',
    version=version,
    author='Dominik Gresch',
    url='http://z2pack.ethz.ch/strain',
    author_email='greschd@gmx.ch',
    install_requires=['numpy', 'pymatgen', 'fsc.export'],
    extras_require={
        'dev': [
            'pytest', 'pre-commit', 'yapf==0.21.0', 'prospector', 'sphinx',
            'sphinx-rtd-theme<0.3'
        ]
    },
    long_description=readme,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English', 'Operating System :: Unix',
        'Development Status :: 3 - Alpha', 'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics'
    ],
    license='GPL',
    packages=find_packages()
)
