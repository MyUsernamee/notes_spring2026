; CIS11
; Delano Leslie
; Lab #2
; Program 2
; Description: A simple LC-3 Program that displays 
; "This is my second program in LC 3!"
; "I am learning assembly programming."

.ORIG x3000
LEA R0, HW
PUTS
HALT
HW .STRINGz "This is my second program in LC 3!\nI am learning assembly programming." ; String stored in memory
.END

