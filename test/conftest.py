#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    18.02.2016 18:07:11 MST
# File:    conftest.py

import pytest
import numpy as np

@pytest.fixture
def structures_close():
    def inner(struc1, struc2):
        assert np.allclose(struc1.lattice.matrix, struc2.lattice.matrix)
        assert len(struc1.sites) == len(struc2.sites)
        for s1, s2 in zip(struc1.sites, struc2.sites):
            assert s1.specie == s2.specie
            assert np.allclose(s1.coords, s2.coords)
    return inner
