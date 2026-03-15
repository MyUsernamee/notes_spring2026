from sympy import *
init_session()

k = 9e9 # N**2/C**2 * m**2
Q = 78.0 * 1e-9 # C
L = 4.70 # m
d = 1.10 # m 

q = Q / L # Charge density

# What is E at d?

dE_x = -x * (k * q / (x**2 + d**2)**(Integer(3)/2))
dE_y = d * (k * q / (x**2 + d**2)**(Integer(3)/2))


# We only care about E_y, and this is symetric across 0 < x < L/2 and -L/2 < x < 0

E_y = 2 * integrate(dE_y, (x, 0, L/2))
E_y


