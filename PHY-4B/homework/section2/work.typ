#import "@preview/cetz:0.4.2": canvas, draw, vector, matrix

== Problem 3

=== Question

You measure an electric field of 1240 N/C at a point 17.2 cm from a small charged particle. 

     (a) Calculate the electric flux through a sphere centered on the particle with a radius equal to this distance;

     (b) Find the magnitude of the charge.

Enter your answer to Part (a), in N-m2/C, in the box below.

=== Work

First we will define all the variables we have.

$ E = 1240 N/C $
$ r = 17.2 times 10^(-2) m $

==== Picture

#canvas({
  import draw: *;
  circle((0, 0, 0),) 
  ortho({
    grid((0, -1, -1), (0, 1, 1), stroke: gray + 0.2pt)
  })
})
==== Part a)

For this, we know the flux through an enclosed surface is equal to the total enclosed charge. This is Guass's Law, or divergence theorem.


