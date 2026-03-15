.orig x3000
ldi r2, y
ldi r3, z
add r2, r2, #1
not r3, r3
add r3, r3, #1 ; R3 = -R3
add r1, r2, r3
sti r1, x
halt

x .fill x3255
y .fill x3300
z .fill x3400

.end
