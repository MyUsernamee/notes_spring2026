
; Calling convention:
; The state of registers is not garunteed.
; All return values will be stored in R0
; Arguments will be passed by r0-r4.

.ORIG x3F00

MULT: ; Multiplies two numbers

    and r0, r0, #0 ; Clear r0
loop_mult:

    add r1, #-1
    brn done
    add r0, r0, r2
    br loop_mult

; end mult

DIV:

    and r0, r0, #0 ; Clear R0
    not r2, r2
    add r2, r2, #1 ; Invert r2
    
loop_div:
    
    add r1, 

; end div

done:
    ret


