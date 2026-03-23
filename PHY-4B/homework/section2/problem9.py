from sympy import *
init_session()

var('N C m', positive=True, real=True)
kg = Symbol("\\text{kg}", positive=True, real=True)
degree = pi / 180

epsilon_naught = 8.854187817e-12 * C**2 / (N * m**2)
g = 9.81 * (N / kg)
mass = 4.20e-3 * kg
q = -6.50e-6 * C
theta = 35.0 * degree

sigma = -epsilon_naught * mass * g * tan(theta) / q
(sigma / (C / m**2)).n() * 1e9
