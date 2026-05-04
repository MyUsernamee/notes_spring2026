from sympy import *
from sympy.physics.units import *
from sympy.physics.units.util import quantity_simplify
init_session()
# %%

e0 = 8.85e-12 * coulomb**2 / (newton * meter**2)

# %%

# Problem #3)

A = 845e-4 * meter ** 2
d = 0.100e-3 * meter
K = 2.10
V = 72.0 * volts

# a)
C = K * e0 * A / (d * 2)
q = C * V
display(convert_to(q.simplify(), [coulomb]))

# b)
U = 1/2 * C * V**2
W = - U / 2
display(convert_to(W, [joule]) * 1e6)

# %%
# Problem #4)

d1 = 1.00 * millimeter
d2 = 2.37 * millimeter

K = 3.17
V = 4.23 * volts

L = 1 * meter

r1 = d1 / 2
r2 = r1 + d2

C = K * 2 * pi * e0 * L / ln(r2 / r1)
U = 1/2 * C * V**2

display(convert_to(U, joules).n() * 1e9)

# %%
# Problem #11)
r1 = 1.00 * centimeters
r2 = 7.40 * centimeters
K1 = 2.2
r3 = 15.0 * centimeters
K2 = 3.10
L = 1.20 * meters
V = 40.0 * volts

Cinner = K1 * 2 * pi * e0 * L / ln(r2 / r1) / 2
Cair = 1 * 2 * pi * e0 * L / ln(r3 / r2) / 2
Coil = K2 * 2 * pi * e0 * L / ln(r3 / r2)

C1 = Cair * Cinner / (Cair + Cinner)
C2 = Coil * Cinner / (Coil + Cinner)

Ctot = C1 + C2

q = Ctot * V

display(convert_to(q, coulomb).n() * 1e9)

# %%

# %%

