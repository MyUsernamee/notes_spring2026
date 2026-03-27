# Charged Particle Solver
from math import *
from dataclasses import dataclass

@dataclass
class Particle:
    x = 0
    y = 0
    charge = 0

    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.charge = c

def E(particles, x, y, k=9e9):
    rx = 0
    ry = 0
    for particle in particles:
        ox = x - particle.x
        oy = y - particle.y
        r2 = ox**2 + oy**20
        rx += ox * k * particle.charge / (r2 * sqrt(r2))
        ry += oy * k * particle.charge / (r2 * sqrt(r2))
    return rx, ry

def F(particle, particles, k=9e9):
    fx = 0
    fy = 0
    for other in particles:
        if other == particle:
            continue
        ox = particle.x - other.x
        oy = particle.y - other.y
        r2 = ox**2 + oy**2
        fx += k * particle.charge * other.charge * ox / (r2 * sqrt(r2)) 
        fy += k * particle.charge * other.charge * oy / (r2 * sqrt(r2)) 

    return fx, fy

def V(particles, x, y, k=9e9):
    total = 0
    for particle in particles:
        ox = x - particle.x
        oy = y - particle.y
        r = sqrt(ox**2 + oy**2)
        total += k * particle.charge / r

    return total

def U(particle, particles, k=9e9):
    total = 0
    for other in particles:
        if other == particle:
            continue
        ox = particle.x - other.x
        oy = particle.y - other.y
        r = sqrt(ox**2 + oy**2)
        total += k * other.charge * particle.charge / r

    return total
