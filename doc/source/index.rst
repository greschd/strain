.. © 2017-2019, ETH Zurich, Institut für Theoretische Physik
.. Author: Dominik Gresch <greschd@gmx.ch>

.. _home:

strain
======

This is a tool to apply strain to crystal structures. Currently it implements only strains for III-V semiconductor materials.

.. contents::
    :local:

Please cite:

* Dominik Gresch, QuanSheng Wu, Georg W. Winkler, Rico Häuselmann, Matthias Troyer, and Alexey A. Soluyanov "Automated construction of symmetrized Wannier-like tight-binding models from ab initio calculations" [`PhysRevMaterials.2.103805 <https://doi.org/10.1103/PhysRevMaterials.2.103805>`_]

* Its refs. [60-66] for the appropriate strain parameters.

The mathematical formulation used to determine the effect of strain can be found in these references.

Installation
------------

You can install this tool with with pip:

.. code ::

    pip install strain

.. toctree::
    :hidden:

    Usage <self>
    reference.rst

Usage
-----

Here we show a simple example usage of the ``strain`` library. First, we define an unstrained structure of InSb using the `pymatgen <http://pymatgen.org>`_ library:

.. ipython::

    In [0]: import pymatgen as mg

    In [0]: a = 3.2395
       ...: structure = mg.Structure(
       ...:     lattice=[[0, a, a], [a, 0, a], [a, a, 0]],
       ...:     species=['In', 'Sb'],
       ...:     coords=[[0] * 3, [0.25] * 3]
       ...: )
       ...: structure

Next, we define the direction and material parameters of the strain to be applied. In the example, we apply biaxial (110) strain. The strain parameters for InSb are given as hard-coded constants in the library, but custom values can also be supplied.

.. ipython::

    In [0]: import strain
       ...: strain_instance = strain.structure.three_five.Biaxial110(**strain.parameter.InSb)

Finally, this strain can be applied to the structure with a given strain strength. For example, to apply :math:`1 \%` positive strain, we set ``strength_multiplier=0.01``.

.. ipython::

    In [0]: strained_structure = strain_instance.apply(structure, strength_multiplier=0.01)
       ...: strained_structure

Note how this does not only change the unit cell, but also appropriately changes the relative position of the atoms.
