from sympy import *
init_session()

var('N m C', positive=True, real=True)

r_inner = 1.40e-2 * m
r_outter = 2.80e-2 * m

Q = 6.35e-6 * C / m**2
q = -0.500e-6 * C

soln = (-q / (4 * pi * r_inner**2)) / (C / m**2)
soln.n() * 1e6


