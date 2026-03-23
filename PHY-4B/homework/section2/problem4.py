from sympy import *
from sympy.abc import N, C, m
init_session(use_unicode=True)

k = 9e-9 * (N * m**2) / C**2

# a)
n_protons = 92
r_nucleus = 7.40e-15 * m
r_electrons = 1.130e-10 * m
q = 1.6e-19 * C

E_nucleus = k * q * n_protons / r_nucleus**2
E_nucleus

# b)

E_electrons = k * q * n_protons / r_electrons**2
E_electrons
