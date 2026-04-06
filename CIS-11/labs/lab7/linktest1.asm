
; linktest1.asm

.ORIG x3F00
.GLOBAL TEST

TEST LD R0, TEST_STRING
    PUTS
    RET

TEST_STRING .STRINGZ "Hello World from linktest1.asm"

.END
