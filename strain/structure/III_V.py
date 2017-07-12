#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>

from __future__ import division, print_function, unicode_literals

from collections import namedtuple

import numpy as np

from .. import CartesianStrain

StrainParameters_III_V = namedtuple(
    'StrainParameters_III_V',
    ['C11', 'C12', 'C44', 'zeta']
)

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

InAs = StrainParameters_III_V(C11=8.329, C12=4.526, C44=3.959, zeta=0.58)
GaSb = StrainParameters_III_V(C11=8.834, C12=4.023, C44=4.322, zeta=0.99)
InSb = StrainParameters_III_V(C11=6.918, C12=3.788, C44=3.132, zeta=0.90)
