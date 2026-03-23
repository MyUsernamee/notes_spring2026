from sympy import *
init_session()

var("N m C", positive=True, real=True)

k = 9e9 * N * m**2 / C**2
q = -2.00e-6 * C
Q = 683e-6 * C / m**3
r = 5.90e-2 * m
d = 10.0e-6 * m

total_q = Q * 4 / 3 * pi * r**3
inner_shell_q = Q * 4 / 3 * pi * d**3

k * total_q / r

