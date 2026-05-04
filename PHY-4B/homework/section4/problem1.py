from sympy import *

kappa = 2.80
epsilon_0 = 8.85e-12
A = 8.90e-4
q = 82.0e-12
V=17.0

d = (kappa * V * epsilon_0 * A) / (q)
d * 1e3
