from sympy import *
from sympy.abc import r, l
init_session()

k = 9e9
Q = 14.4e-9 # C
R = 61.6e-2 # M
x = 83.0e-2 # M

A = pi * R**2
q = Q / A

d = sqrt(x**2 + r**2)
dE = x / d * k * q / d**2
E = integrate(dE, (l, 0, 2 * pi * r), (r, 0, R))
E
