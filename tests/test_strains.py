import os
import pytest
import time
import pymatgen as mg

from strain import parameter
from strain.structure import three_five

INITIAL_STRUCTURE = mg.structure.Structure.from_file('samples/POSCAR')

@pytest.mark.parametrize(['strain_instance', 'strength', 'reference_file'],
    [
        (three_five.Biaxial001(**parameter.InSb), 0.04, 'POSCAR_001_bi_0.04'),
        (three_five.Biaxial110(**parameter.InSb), 0.04, 'POSCAR_110_bi_0.04'),
        (three_five.Biaxial111(**parameter.InSb), 0.04, 'POSCAR_111_bi_0.04'),
        (three_five.Uniaxial110(**parameter.InSb), 0.04, 'POSCAR_100_uni_0.04'),
    ]
)
def test_strain(strain_instance, strength, reference_file, structures_close):
    reference_struc = mg.structure.Structure.from_file(os.path.join('samples', reference_file))
    res_struc = strain_instance.apply(INITIAL_STRUCTURE, strength_multiplier=strength)
    structures_close(res_struc, reference_struc)
