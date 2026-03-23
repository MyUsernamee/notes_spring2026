from sympy import *
init_session()

var('N m C q', positive=True, real=True)

k = 9e9 * N * m**2 / C**2
d = 52.0e-2 * m
E = 914 * N / C
delta_x = 2.80e-2 * m

direction = Matrix((x, d))

eq = Eq(E, k * q * integrate(direction / sqrt(x**2 + d**2) ** 3, (x, -oo, oo), manual=True)[1])
eq
soln = solve(eq, q)[0]
soln
soln * delta_x * 1e9

