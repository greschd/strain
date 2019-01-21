#!/usr/bin/env python
# -*- coding: utf-8 -*-

# © 2017-2019, ETH Zurich, Institut für Theoretische Physik
# Author: Dominik Gresch <greschd@gmx.ch>
"""
A module for applying strains to crystal structures.
"""

from ._strain import *
from . import structure
from . import parameter

__version__ = '0.2.1'

__all__ = ['__version__', 'structure', 'parameter'] + _strain.__all__  # pylint: disable=undefined-variable
