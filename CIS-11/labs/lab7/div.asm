; div.asm
; Provides a very simplistic division routine.
; To use, assemble, load .obj, and jsr to .ORIG

; Calling convention
; State of registers after running isn't guarenteed
; R0 -> Return Value
; R1-R5 -> Arguments

.ORIG x3E00

DIVIDE ; Multiplies two numbers
    and r0, r0, #0 ; Clear r0

    not r2, r2
    add r2, r2, #1 ; R2 = -R2

loop_div
    add r1, r1, r2
    brzn done

    add r0, r0, #1 
    br loop_mult
    
done 
    not r1, r1
    add r1, r1, #1 ; R1 = -R1 (Remainder)
    ret

.END
