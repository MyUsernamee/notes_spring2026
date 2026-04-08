; test.asm
; Tests mult.asm, and div.asm

.ORIG x3000

MAIN
    lea R6, STACK
    str R7, R6, #0
    add R6, R6, #1
    jsr TEST_MULT
    jsr TEST_DIV
    halt

TEST_MULT
    str R7, R6, #0
    add R6, R6, #1 ; New stack frame.
    ld R1, X 
    ld R2, Y
    ld R3, MULT

    jsrr R3 ; MULT 
    ld R2, MULT_TEST_EXPECTED
    and r1, r1, #0
    add r1, r1, r0
    jsr ASSERT_EQ

    add R6, R6, #-1
    ldr R7, R6, #-1
    ret

TEST_DIV
    ret ; Not Implemented

ASSERT_EQ ; If R1==R2, Halts, and prints output if not.
    str R7, R6, #0
    add R6, R6, #1 ; New stack frame.
    not r1, r1
    add r1, r1, #1

    add r2, r2, r1

    brz success
    
    lea R0, ASSERT_MESSAGE
    puts
    halt

success
    add R6, R6, #-1
    ldr R7, R6, #-1
    ret

; end ASSERT_EQ

; DATA

ASSERT_MESSAGE .STRINGZ "Assertion failed."
MULT_TEST_EXPECTED .FILL #15
X .FILL #3
Y .FILL #5
MULT .FILL x3F00

STACK .BLKW xFF

.END
