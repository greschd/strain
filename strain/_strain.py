import six
import abc
import copy

import numpy as np
from fsc.export import export
import pymatgen as mg
from pymatgen.analysis.elasticity.strain import Deformation


@export
class Strain(six.with_metaclass(abc.ABCMeta, object)):
    """
    Base class for applying strain to a structure.
    """

    @abc.abstractmethod
    def apply(structure, strength_multiplier=1.):
        """
        Apply the strain to a given structure.

        :param structure: Input structure
        :type structure: pymatgen.Structure

        :param strength_multiplier: Strength of the strain
        :type strength_multiplier: float
        """
        raise NotImplementedError


@export
class CartesianStrain(Strain):
    """
    Applies a strain given in cartesian coordinates to the structure.

    :param deformation_matrix: Matrix describing the deformation of the unit cell.
    :type deformation_matrix: array

    :param pos_displacement_matrices: Matrices describing the displacement of each of the atom positions.
    :type pos_displacement_matrices: array
    """

    def __init__(self, deformation_matrix, pos_displacement_matrices=None):
        self.deformation_matrix = deformation_matrix
        self.pos_displacement_matrices = pos_displacement_matrices

    def apply(self, structure, strength_multiplier=1.):
        deformation = Deformation(
            np.eye(3) + strength_multiplier * self.deformation_matrix
        )
        new_structure = deformation.apply_to_structure(structure)
        # move positions
        if self.pos_displacement_matrices is not None:
            for idx, mat in self.pos_displacement_matrices:
                new_structure.translate_sites(
                    indices=[idx],
                    # use original cartesian positions
                    vector=strength_multiplier *
                    np.dot(mat, structure.cart_coords[idx]),
                    frac_coords=False
                )
        return new_structure
