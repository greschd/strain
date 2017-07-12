from __future__ import division, print_function, unicode_literals

import types

import numpy as np

from .. import CartesianStrain

class StrainParameters_III_V(dict):
    def __init__(self, C11, C12, C44, zeta):
        self['C11'] = C11
        self['C12'] = C12
        self['C44'] = C44
        self['zeta'] = zeta

class Biaxial001(CartesianStrain):
    def __init__(self, C11, C12, C44, zeta):
        exx = eyy = 1
        ezz = -2 * C12 / C11
        super(Biaxial001, self).__init__(deformation_matrix=np.diag([exx, eyy, ezz]))

class Biaxial110(CartesianStrain):
    def __init__(self, C11, C12, C44, zeta):
        ezz = 1
        exx = (2 * C44 - C12) / (2 * C44 + C11 + C12)
        exy = (-C11 - 2 * C12) / (2 * C44 + C11 + C12)
        deformation_matrix = np.array([
            [exx, exy, 0],
            [exy, exx, 0],
            [0,   0, ezz]
        ])
        pos_displacement_matrices = [
            (1, -2 * exy * zeta * np.diag([0, 0, 1]))
        ]
        super(Biaxial110, self).__init__(
            deformation_matrix=deformation_matrix,
            pos_displacement_matrices=pos_displacement_matrices
        )

class Biaxial111(CartesianStrain):
    def __init__(self, C11, C12, C44, zeta):
        exx = 4 * C44 / (4 * C44 + C11 + 2 * C12)
        exy = (-C11 - 2 * C12) / (4 * C44 + C11 + 2 *C12)
        deformation_matrix = np.array([
            [exx, exy, exy],
            [exy, exx, exy],
            [exy, exy, exx]
        ])
        pos_displacement_matrices = [
            (1, -2 * exy * zeta * np.eye(3))
        ]
        super(Biaxial111, self).__init__(
            deformation_matrix=deformation_matrix,
            pos_displacement_matrices=pos_displacement_matrices
        )

class Uniaxial110(CartesianStrain):
    def __init__(self, C11, C12, C44, zeta):
        ezz = 1
        exx = -C11 / (2 * C12)
        exy = -(C11 - C12) * (C11 + 2 * C12) / (4 * C44 * C12)
        deformation_matrix = np.array([
            [exx, exy, 0],
            [exy, exx, 0],
            [0,   0, ezz]
        ])
        pos_displacement_matrices = [
            (1, -2 * exy * zeta * np.diag([0, 0, 1]))
        ]
        super(Uniaxial110, self).__init__(
            deformation_matrix=deformation_matrix,
            pos_displacement_matrices=pos_displacement_matrices
        )
