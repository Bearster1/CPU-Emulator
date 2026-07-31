Data 27 # The answer number.
Data "X" # The Wrong Answer text
Data "O" # The Correct Answer text
Data "\n" # New line
label loop
In A
Acc = RAM[0]
Sub A
C = label correct
if Acc = 0: Jump C

B = RAM[1]
Out B
B = RAM[3]
Out B
B = label loop
if B > 0: Jump B

label correct
B = RAM[2]
Out B
STOP