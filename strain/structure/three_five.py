"""
This module contains classes for different kinds of strain applied to III-V semiconductor materials.
"""

from __future__ import division, print_function, unicode_literals

import numpy as np
from fsc.export import export

from .. import CartesianStrain


@export  # pylint: disable=invalid-name
class StrainParameters_III_V(dict):
    """
    Data class containing the strain parameters for III-V semiconductors.
    """

    def __init__(self, C11, C12, C44, zeta):
        super(StrainParameters_III_V, self).__init__()
        self['C11'] = C11
        self['C12'] = C12
        self['C44'] = C44
        self['zeta'] = zeta


@export
class Biaxial001(CartesianStrain):
    """
    Bi-axial [001] strain for III-V semiconductors.
    """

    def __init__(self, C11, C12, C44, zeta):  # pylint: disable=unused-argument
        exx = eyy = 1
        ezz = -2 * C12 / C11
        super(Biaxial001,
              self).__init__(deformation_matrix=np.diag([exx, eyy, ezz]))


@export
class Biaxial110(CartesianStrain):
    """
    Bi-axial [110] strain for III-V semiconductors.
    """

    def __init__(self, C11, C12, C44, zeta):
        ezz = 1
        exx = (2 * C44 - C12) / (2 * C44 + C11 + C12)
        exy = (-C11 - 2 * C12) / (2 * C44 + C11 + C12)
        deformation_matrix = np.array([[exx, exy, 0], [exy, exx, 0],
                                       [0, 0, ezz]])
        pos_displacement_matrices = [(1, -2 * exy * zeta * np.diag([0, 0, 1]))]
        super(Biaxial110, self).__init__(
            deformation_matrix=deformation_matrix,
            pos_displacement_matrices=pos_displacement_matrices
        )


@export
class Biaxial111(CartesianStrain):
    """
    Bi-axial [111] strain for III-V semiconductors.
    """

    def __init__(self, C11, C12, C44, zeta):
        exx = 4 * C44 / (4 * C44 + C11 + 2 * C12)
        exy = (-C11 - 2 * C12) / (4 * C44 + C11 + 2 * C12)
        deformation_matrix = np.array([[exx, exy, exy], [exy, exx, exy],
                                       [exy, exy, exx]])
        pos_displacement_matrices = [(1, -2 * exy * zeta * np.eye(3))]
        super(Biaxial111, self).__init__(
            deformation_matrix=deformation_matrix,
            pos_displacement_matrices=pos_displacement_matrices
        )


@export
class Uniaxial110(CartesianStrain):
    """
    Uni-axial (110) strain for III-V semiconductors.
    """

    def __init__(self, C11, C12, C44, zeta):
        ezz = 1
        exx = -C11 / (2 * C12)
        exy = -(C11 - C12) * (C11 + 2 * C12) / (4 * C44 * C12)
        deformation_matrix = np.array([[exx, exy, 0], [exy, exx, 0],
                                       [0, 0, ezz]])
        pos_displacement_matrices = [(1, -2 * exy * zeta * np.diag([0, 0, 1]))]
        super(Uniaxial110, self).__init__(
            deformation_matrix=deformation_matrix,
            pos_displacement_matrices=pos_displacement_matrices
        )
