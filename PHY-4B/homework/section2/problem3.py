from sympy import *
from sympy.abc import N, C, m
init_session(use_unicode=True)

E = 1240 * N / C
d = 17.2e-2 * m

flux = 4 * pi * d**2 * E
(flux / ((N * m**2) / C)).n()

