from sympy import *
init_session()

k = 9e9
E = 815 # N/m

m_p = 1.67e-27 # kg
m_e = 9.11e-31 # ke

q_p = 1.60e-19 # C
q_e = -1.60e-19 # C

F_p = q_p * E
F_e = q_e * E

a_p = F_p / m_p
a_e = F_e / m_e

print(a_e)
