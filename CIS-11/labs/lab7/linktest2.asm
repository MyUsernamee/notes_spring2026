
; linktest2.asm

.ORIG x3100
.EXTERNAL TEST

JSR TEST

LD R0, TEST_STRING
PUTS

HALT

TEST_STRING .STRINGZ "Hello World from linktest2.asm"

.END
