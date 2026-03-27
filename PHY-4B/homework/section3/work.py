import numpy as np

k = 9e9
q = 13.0e-6
s = 55.0e-2

positions = []
for i in range (2):
    for j in range (2):
        for k in range (2):
            positions.append(((i - 0.5) * s,( j - 0.5) * s,( k - 0.5) * s))

def V(p, q, k=9e9):
    dists = [np.sqrt(sum([(a - b)**2 for a, b in zip(c, p)])) for c in positions]
    pots = [k * q / r for r in dists]
    return sum(pots)

V((0, 0, s/2), q) * 1e-3
