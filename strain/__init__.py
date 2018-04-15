"""
A module for applying strains to crystal structures.
"""

from ._version import __version__
from ._strain import *
from . import structure
from . import parameter

__all__ = ['__version__', 'structure', 'parameter'] + _strain.__all__  # pylint: disable=undefined-variable
