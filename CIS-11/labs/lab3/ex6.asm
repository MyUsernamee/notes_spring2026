.orig x3000
and r1, r1, x0
and r2, r2, x0
ld r6, reset
lea r0, line1
puts
getc
out
add r1, r6, r0
lea r0, line2
puts
getc
out
add r2, r6, r0
jsr compare
halt

compare
        and r3, r3, x0
        not r2, r2
        add r2, r2, x1
        add r3, r1, r2
        brn neg
            add r3, r3, x0
        brp pos
            add r3, r3, x0
        brz eq
            and r5, r5, x0
            add r5, r5, r1
        ret
    neg lea r0, n
        puts
        ret
    pos lea r0, p
        puts
        ret
    eq lea r0, e
        puts
        ret

; Data
n .stringz "\nX is less than Y"
p .stringz "\nX is greater than Y"
e .stringz "\nX is equal to Y"
reset .fill xFFd0
line1 .stringz "Enter X:"
line2 .stringz "\nEnter Y:"
.end

