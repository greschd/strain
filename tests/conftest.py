"""
Configuration file for pytest tests.
"""

import pytest
import numpy as np


@pytest.fixture
def structures_close():
    """
    Fixture that tests whether two structures are approximately equal.
    """

    def inner(struc1, struc2):  # pylint: disable=missing-docstring
        assert np.allclose(struc1.lattice.matrix, struc2.lattice.matrix)
        assert len(struc1.sites) == len(struc2.sites)
        for site1, site2 in zip(struc1.sites, struc2.sites):
            assert site1.specie == site2.specie
            assert np.allclose(site1.coords, site2.coords)

    return inner
