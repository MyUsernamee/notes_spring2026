.orig x3000
ldi r3, p
ldi r4, q
not r2, r4
add r2, r2, #1
add r1, r2, r3
sti r1, minus
halt

p .fill x3120
q .fill x3121
minus .fill x3122

.end
