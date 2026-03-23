from sympy import *
from sympy.abc import Q, q, E, tau, theta, d
from sympy.abc import N, C, m

subs = {tau: 7.20e-9 * (N * m), q: 4.20e-9 * C, d: 3.10e-3 * m, theta: 32.0 / 180.0 * pi}

F = q * E
eq = F * d * sin(theta) - tau

soln = solve(eq, E)[0].subs(subs) / (N / C)
soln.n()

