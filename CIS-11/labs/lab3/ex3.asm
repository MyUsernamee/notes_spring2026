.orig x3000
ld r0, A ; Load data into registers
ld r2, nine
ld r1, B
ld r3, C
ld r5, T

; Invert r2
not r2, r2
add r2, r2, x1

; Perform calculation. Addition is communative
add r2, r2, r0
add r2, r2, r1
add r2, r2, r3

str r2, r5, x0 ; Save calculation.

halt

A .fill x3102
B .fill x3103
C .fill x3104
T .fill x3105
nine .fill x9

.end
