#!/usr/bin/env python
# -*- coding: utf-8 -*-

# © 2017-2019, ETH Zurich, Institut für Theoretische Physik
# Author: Dominik Gresch <greschd@gmx.ch>
"""
Test strains for III-V semiconductors.
"""

import os

import pytest
import pymatgen as mg

from strain import parameter
from strain.structure import three_five

INITIAL_STRUCTURE = mg.structure.Structure.from_file('samples/POSCAR')  # pylint: disable=no-member


@pytest.mark.parametrize(['strain_instance', 'strength', 'reference_file'], [
    (three_five.Biaxial001(**parameter.InSb), 0.04, 'POSCAR_001_bi_0.04'),
    (three_five.Biaxial110(**parameter.InSb), 0.04, 'POSCAR_110_bi_0.04'),
    (three_five.Biaxial111(**parameter.InSb), 0.04, 'POSCAR_111_bi_0.04'),
    (three_five.Uniaxial110(**parameter.InSb), 0.04, 'POSCAR_100_uni_0.04'),
])
def test_strain(strain_instance, strength, reference_file, structures_close):
    """
    Test that strained structures match the reference files.
    """
    reference_struc = mg.structure.Structure.from_file(  # pylint: disable=no-member
        os.path.join('samples', reference_file)
    )
    res_struc = strain_instance.apply(
        INITIAL_STRUCTURE, strength_multiplier=strength
    )
    structures_close(res_struc, reference_struc)
