.ORIG x3000

ldi r0, n

 ; Clear registers
and r1, r1, x0 ; F
and r2, r2, x0 ; a
and r3, r3, x0 ; b
and r4, r4, x0

add r4, r4, x3
not r4, r4
add r4, r4, x1

add r2, r0, r4
BRn nlt2
BR nlt2_else

nlt2
add r1, r1, x1
BR done

nlt2_else
and r2, r2, x0
add r2, r2, x1
add r3, r3, x1

and r4, r4, x0 ; -i
add r4, r4, x3
not r4, r4
add r4, r4, x1

loop

    add r5, r4, r0
    brn done

    add r1, r2, r3 ; F = a + b

    brn overflow
    
    and r2, r2, x0
    add r2, r2, r3 ; a = b

    and r3, r3, x0
    add r3, r3, r1 ; b = F

    add r4, r4, xffff ; i=i-1
    br loop

overflow
not r4, r4
add r4, r4, x1
sti r4, oN
sti r1, oFN
halt

done
sti r1, Fn
halt

n .FILL x3100
Fn .FILL x3101
oN .FILL x3102
oFN .FILL x3103

.END
