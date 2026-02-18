#import "@local/booklet:0.1.0": *;
#set page(width: 11in/2, height: 8.5in)

// 3-12 odd, 27-39 odd

#booklet([12.1], (
  (3, [Which of the points $A(-4, 0, -1)$, $B(3, 1, -5)$, and $C(2, 4, 6)$, is the closest to the yz-plane? Which point lies in the xz-plane?]),
  (5, [What does the equation $x=3$ represent in $RR^2$? What does it represent in $RR^3$? Illustrate with sketches.]),
  (7, [Describe and sketch the surface in $RR^3$, represented by the equation $x + y = 2$.]),
  (9, [Find the distance between the given points: $(3, 5, -2)$, $(-1, 1, -4)$]),
  (11, [Find the lengths of the sides of the triangle $P Q R$. Is it a right triangle? Is it an isosceles triangle? $P(3, -2, -3)$, $Q(7, 0, 1)$, $R(1, 2, 1)$]),
  ([27-39], [Describe in words the region of $RR^3$ represent by the equation(s) or inequalities.]),
  (27, [$z=-2$]),
  (29, [$y >= 1$]),
  (31, [$-1 <= x <= 2$]),
  (33, [$x^2 + y^2 = 1$, $z=-1$]),
  (35, [$y^2 + z^2 <= 25$]),
  (37, [$x^2 + y^2 + z^2 = 4$]),
  (39, [$1 <= x^2 + y^2 + z^2 <= 5$])
), (
  (3, [C; A]),
  (5, [A line parallel to the y-axis and 4 unites to the right of it; a vertical plane parallel to the yz-plane and 4 units in front of it.]),
  (7, [A vertical plane the intersects the xy-plane in the line $y=2-x$, $z=0$]),
  (9, 6),
  (11, [$|P Q| = 6$, $|Q R| = 2 sqrt(10)$, $|R P| = 6$; isosceles triangle]),
  (27, [A horizontal plane 2 units below the xy-plane]),
  (29, [A half-space consisting of all points on or to the right of the plane $y=1$]),
  (31, [All points on or between the vertical planes $x=-1$, and $x=2$]),
  (33, [All points on a circle with radius 2 and center on the z-axis that is contained in the plane $z=-1$]),
  (35, [All points on or inside a circular cylinder of radius 5 with axis the x-axis]),
  (37, [All points on a sphere with radius 2 and center $(0, 0, 0)$]),
  (39, [All points on or between spheres with radii $1$ and $sqrt(5)$ and centers $0, 0, 0)$])
))
