from math import *

k = 9e9 # (N m^2 / C^2)
q1 = 12.0e-6 # C
q2 = 24.0e-6 # C
q3 = 38.0e-6 # C
a = 40.0e-2 # m 
b = 65.0e-2 # m 

U = k * (q1 * q2 / a + q1 * q3 / sqrt(a**2 + b**2) + q2 * q3 / b)
U
