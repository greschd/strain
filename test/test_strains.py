#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>

import os
import pytest
import time
import pymatgen as mg

import strain_III_V as st

INITIAL_STRUCTURE = mg.structure.Structure.from_file('samples/POSCAR')

@pytest.mark.parametrize(['strain_instance', 'strength', 'reference_file'],
    [
        (st.Biaxial001(**st.InSb._asdict()), 0.04, 'POSCAR_001_bi_0.04'),
        (st.Biaxial110(**st.InSb._asdict()), 0.04, 'POSCAR_110_bi_0.04'),
        (st.Biaxial111(**st.InSb._asdict()), 0.04, 'POSCAR_111_bi_0.04'),
        (st.Uniaxial110(**st.InSb._asdict()), 0.04, 'POSCAR_100_uni_0.04'),
    ]
)
def test_strain(strain_instance, strength, reference_file, structures_close):
    reference_struc = mg.structure.Structure.from_file(os.path.join('samples', reference_file))
    res_struc = strain_instance.apply(INITIAL_STRUCTURE, strength_multiplier=strength)
    print(res_struc.frac_coords)
    print(reference_struc.frac_coords)
    structures_close(res_struc, reference_struc)
