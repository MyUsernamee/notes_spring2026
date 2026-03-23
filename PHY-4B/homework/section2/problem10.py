from sympy import *
init_session()

var('N C m', positive=True, real=True)
epsilon_naught = 8.854187817e-12 * C**2 / (N * m**2)

a = 1.30 * m
b = 2.50 * m
c = 3.80 * m

E1 = 500 * N / C
E2 = 700 * N / C
E3 = 900 * N / C

q_enc = 2 * epsilon_naught * (a * b * E1 + a * c * E2 + b * c * E3)
q_enc * 1e9
