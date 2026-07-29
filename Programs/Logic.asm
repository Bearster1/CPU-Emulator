in A # Data A
in B # Data B
in C # Command: Negative = Not 0 = And Positive = Or
Acc = 9
if C > 0: Jump Acc
Acc = 19
if C = 0: Jump Acc
Acc = 25
if C < 0: Jump Acc
Acc = A # OR: NOT(A) NAND NOT(B)
NAND A
A = Acc
Acc = B
NAND B
B = Acc
NAND A
C = Acc
out C
STOP
Acc = A # AND: NOT(A NAND B)
NAND B
NAND Acc
C = Acc
out C
STOP
Acc = A # NOT(A)
NAND A
C = Acc
out C
STOP