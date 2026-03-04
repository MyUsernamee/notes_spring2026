from sympy import *
from sympy.abc import *

k = 9e9

# Four identical charged particles are arranged at the corners of a rectangle, as shown. The particles each have charge 22.0 nC and the rectangle has dimensions a = 68.0 cm and b = 44.0 cm. Find the magnitude of the total electric field, due to all four particles, at:
#
#      (a) the center of the rectangle;
#
#      (b) the center of one of the longer sides of the rectangle;
#
#      (c) the center of one of the shorter sides of the rectangle.
#
# Enter your answer for Part (c), in N/C, in the box below.

q = 22.0e-9
a = 68.0e-2
b = 44.0e-2

# Part a)
# This one is quite simple, one can easily reason that, due to the identical charges, and symetry, there must be no force.

# Part c)

# We can assume that the force due to the particles directly above and below have canceling forces.
# This only leaves the two other particles which are symetric vertically, so all we really must do it calculate the
# Horizontal components of one and double it.
# We can also assume vertical forces cancel.

center_left_distance = sqrt((b/2)**2 + a**2)
sin_theta = a/center_left_distance
total_horizontal_force = 2 * (k * q / (center_left_distance ** 2) * sin_theta)
sin_theta
total_horizontal_force

