from sympy import *
init_session()

q = 6.20e-11 # C
m = 4.10e-13 # kg
E = 292.0 # N/C

F = q * E
a = F / m
a # Part a)

v = integrate(a, t)
v # Part b)
x = integrate(v, (t, 0, 3e-3))
x # Part c)
