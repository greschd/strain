#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .structure.three_five import StrainParameters_III_V

InAs = StrainParameters_III_V(C11=8.329, C12=4.526, C44=3.959, zeta=0.58)
GaSb = StrainParameters_III_V(C11=8.834, C12=4.023, C44=4.322, zeta=0.99)
InSb = StrainParameters_III_V(C11=6.918, C12=3.788, C44=3.132, zeta=0.90)
