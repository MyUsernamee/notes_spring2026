; mult.asm
; Provides a very simplistic multiplication routine.
; To use, assemble, load .obj, and jsr to .ORIG

; Calling convention
; State of registers after running isn't guarenteed
; R0 -> Return Value
; R1-R5 -> Arguments

.ORIG x3F00

MULT ; Multiplies two numbers
    str R7, R6, #0
    add R6, R6, #1 ; New stack frame.

    and r0, r0, #0 ; Clear r0

loop_mult
    add r1, r1, #-1
    brn done
    add r0, r0, r2
    br loop_mult
    
done 
    add R6, R6, #-1
    ldr R7, R6, #-1
    ret

.END

