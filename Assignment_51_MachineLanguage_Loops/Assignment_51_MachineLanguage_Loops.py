# Joey Fong
# joey.fong39@myhunter.cuny.edu

ADDI $s0, $zero, 2 
ADDI $s1, $zero, 2
ADDI $s2, $zero, 20

AGAIN: ADDI $s0, $s0, 2

BEQ $s0, $s2, DONE

J AGAIN
DONE:


