from sympy import *
from sympy.abc import k, Q, R, x, L, theta, phi, l
init_session()
"""
Charge Q = 25.6 uC is uniformly distributed around a ring of radius R = 0.443 m. Find the magnitude and direction of the electric field at a point x = 1.3 m from the center of the ring, along the axis of the ring (as shown below). 

Enter your answer, in N/C, in the box below.
"""

k = 9e9
Q = 27.2e-6 # C
R = 0.427 # m
x = 1.1 # m


L = 2 * pi * R # Circumfrence of ring

# We can imagine the ring like a "planet"
# Because R<x, the total ring "feels like" a single point mass at the center of the ring. The question then is what is the "mass" (charge) of this imaginary particle. Well as the particle moves very far away from the center of the ring, it behaves like a particle. The angle between the normal of the ring and the particle's offset approaches 90. Which means all of the charge on the ring should just behave like a single particle. When the particle is in the middle of the ring, it should feel no force. So, the "appearnt ratio of mass" of the imaginary particle is sin theta. (This is speculation, but there is a proof). So the Charge is 

sin_theta = x / sqrt(x**2 + R**2) # Opposite over Hypotnuse

E = k * Q * sin_theta / (x**2 + R**2)
E

L = 2 * pi * R
q = Q / L
expr = k * q / (x**2 + R**2) * (x / sqrt(x**2 + R**2))
E = integrate(expr, (l, 0, L))
E
