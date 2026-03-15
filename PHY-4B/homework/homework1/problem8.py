from sympy import *
init_session()

"""
A particle with mass 1.20 milligrams and charge 25.0 uC initially moves in a horizontal direction with speed v = 85.0 m/s, as shown. The particle enters a region between two horizontal plates at a point d = 14.0 cm above the lower plate. The particle is deflected by a vertical electric field of magnitude E = 2230 N/C such that it just misses the edge of the lower plate. Find:

    (a) the time the particle is between the plates;      

    (b) the length of the plates, L, in cm.

Enter your answer for Part (b) in the box below
"""

m = 1.60e-6 # kg
q = 25e-6 # C
v = 85.0 # m/s
d = 14.0e-2 # m
E = 2440 # N/C

F = -q * E
a = F / m

x_t = integrate(a, t)
x = integrate(x_t, t) + d
t = solve(x, t)[1] # Part a)

L = v * t
L * 100 # Part b)
