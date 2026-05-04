from sympy import *
init_session()

# %%
# Problem #4)

R1 = 425 # Ohms
R2 = 680 # Ohms
Vb = 12.8 # V

W2 = Vb**2 / R2
W2

# %%
# Problem #5)

R1 = 225 # Ohms
R2 = 377 # Ohms
Vb = 15.2 # V
I = Vb / (R1 + R2)
W2 = I**2 * R2
print(W2)

# %%

