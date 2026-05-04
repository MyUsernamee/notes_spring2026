from sympy import *
from sympy.physics.units import *
init_session()
# %%
# Problem #3)
rate = 0.28 / (watts * 1e3 * hour)

P = 240 * volts * 9.50 * amperes * 41.0 * minutes
display(convert_to(P, [watt, hour]) * rate)

# %%
# Problem #6)

V = 315 * volts
A = 38.7 * amperes
Wm = 10.2e3 * watts
density = 0.920 * grams / centimeter**3
c = 3.80 * joules / (grams * kelvin)
DT = 3.00 * kelvin

P = convert_to(V * A, watts)
q = convert_to(P - Wm, [joules, seconds])
m = convert_to(q / (c*DT), grams)
V = convert_to(m / density, centimeter)

display(convert_to(expand(V), [grams, seconds]))

# %%
# Problem #7)

I1 = 17.0e-3 * amperes
I2 = 92.0e-3 * amperes
R1 = 235 * ohms

R2, V = symbols('R2 V')

Rs = R1 + R2
Rp = R1 * R2 / (R1 + R2)

eq1 = Eq(V, I1 * Rs)
eq2 = Eq(V, I2 * Rp)

solve([eq1, eq2])

# %%
# Problem #8)

Ra, Rb, Rc, Rd, Re = tuple(i * ohms for i in [134, 183, 209, 290, 318])
V = 18.0 * volts

Rbd = Rb + Rd
Rcbd = Rbd * Rc / (Rbd + Rc)
Rabcde = Ra + Rcbd + Re

I = V / Rabcde

# Current of resistors in series but be equal, so Ia == Icbd == Ie == I
# Va + Vcbd + Ve == V
# Icbd == I
# Vcbd / Rcbd == I
# Vcbd / Rcbd == I
# Vc == Vbd == Vcbd
# Ic * Rc == Vcbd
# Ic * Rc / Rcbd == I
# Ic ==  I * Rcbd / Rc

Ic = I * Rcbd / Rc
display(convert_to(Ic.simplify() * 1e3, amperes))

# %%
# Problem #9)
Ra, Rb, Rc, Rd, Re = tuple(i * ohms for i in [126, 182, 227, 284, 308])
V = 24.0 * volts

Rbc = (Rb * Rc) / (Rb + Rc)
Rbcd = (Rbc * Rd) / (Rbc + Rd)
Rtot = Ra + Rbcd + Re

# a)
display(Rtot.n())

# b)
I = V / Rtot
display(I)

# c)
# Ia == Ibcd == Ie == I
# Ibcd == I
# Vbcd / Rbcd == I
# Vb == Vc == Vd == Vbcd
# Vc / Rbcd == I
# Ic * Rc / Rbcd == I
# Ic == I * Rbcd / Rc

Ic = I * Rbcd / Rc
display(convert_to(Ic.n() * 1e3, amperes))

# %%
# Problem #10)
Ra, Rb, Rc, Rd, Re = tuple(i * ohms for i in [137, 194, 209, 264, 307])
V1 = 18.0 * volts
V3 = 14.0 * volts 

Rab = Ra + Rb
Rde = Rd + Re
Rabc = Rab + Rc
Rcde = Rde + Rc

Vab, Vde, Ic = symbols('Vab Vde Ic')

eq1 = Vab + Ic * Rc - V1
eq2 = Vde + Ic * Rc - V3
eq3 = Vab / Rab + Vde / Rde - Ic

display(convert_to(solve([eq1, eq2, eq3])[Ic], amperes) * 1e3)

# %%
# Problem #11)
V = 12.0 * volts
R = 250 * ohms

