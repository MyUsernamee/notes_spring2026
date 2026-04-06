"""A particle of mass 4.70 x 10-12 kg moves in a straight line with speed 3300 m/s. It enters an electric field of 7700 N/C that is in a direction opposite that of the particle’s velocity. The particle is brought to rest while it travels a distance of 25.0 cm against the field. Find:

    (a) the change in kinetic energy of the particle;

    (b) the change in potential energy of the particle;

    (c) the charge of the particle.

Enter your answer to Part (c), in nC, in the box below."""

from sympy import *
init_session()

m = 4.70e-12
s = 3300
E = 7700
d = 25.0e-2

var('q')

Ek = 0.5 * m * s**2
Fe = q * E
Ep = Fe * d

solve(Ep - Ek, q)[0] * 1e9


