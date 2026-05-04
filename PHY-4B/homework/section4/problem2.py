from sympy import *

# %%
# You want to design a parallel plate capacitor to have a capacitance of 128 nF and a maximum potential of 430 Volts. 
# You choose polycarbonate for a dielectric, which has a dielectric constant of 
# 2.80 and a dielectric strength (i.e. the maximum electric field it can withstand) of 3.00 x 107 V/m.
# Find the minimum area of the plates that you will need to build this capacitor.

C = 121e-9 # F
V_max = 450 # V
kappa = 2.80
E_max = 3.00e7 # V/m

e_0 = 8.85e-12 # C^2/N-m^2
k = 8.99e9 # N-m^2/C^2

A, d, sigma = symbols('A d sigma', positive=True, real=True)

eq1 = Eq(C, (kappa * e_0 * A) / d)
q = C * V_max
eq2 = Eq(E_max, k * q / d)

# %%

solve([eq1, eq2], [A, d])[A] * 1e1

# %%

