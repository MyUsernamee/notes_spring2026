from sympy import *
from sympy.abc import m, C, s
init_session()

kg = symbols('\\text{kg}')
N = (kg * m / s**2)

q = 6.5e-9 * C
E = 1000 * N / C
d = 2.40e-3 * m
m = 1.20e-9 * kg

omega = sqrt(q * E / (m * d))
posify(omega * s)[0]
