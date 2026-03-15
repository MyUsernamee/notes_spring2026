.orig x3000

ld r0, p
ld r1, q
ld r2, s ; Load information.
ld r3, z
ld r4, offset 
add r3, r3, r4 ; Add 0x4D to Z

str r3, r0, #0
str r3, r1, #0
str r3, r2, #0 ; Save results

halt

p .fill x3100
q .fill x3200
s .fill x3300
z .fill x3400
offset .fill x4d

.end
