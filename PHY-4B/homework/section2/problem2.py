from sympy import *
init_session()

var('N C m', positive=True, real=True)
epsilon_naught = 8.854187817e-12 * C**2 / (N * m**2)
kg = Symbol("\\text{kg}", positive=True, real=True)
degree = pi / 180

q = 6.40e-9 * C
m = 1.5e-9 * kg
d = 2.50e-3 * m
E = 1000 * N / C

F = E * q / m
f = 1/(2 * pi) * sqrt(2 * F / d)
(f / sqrt(N)).n()
