from math import *
from solver import * 
from sympy import *

q = 22.0e-6 # C
a = 62.0e-2 # m
b = 37.0e-2 # m

particles = []

for i in range(2):
    for j in range(2):
        particles.append(Particle(a * (i - 0.5), b * (j - 0.5), q))


V_soln = V(particles, a / 2, 0)
V_soln * 1e-3


