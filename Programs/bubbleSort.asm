Data 5
Data 3
Data 4
Data 1
Data 2
C = 4 # Num Data Points here (-1)
A = RAM[C] # Label 1 would go here jumping while C > 0
Acc = C
B = 1
Sub B
Acc = RAM[Acc]
Sub A
A = 22 # Jump 2 Address # 17 + Num Data Points
if Acc > 0: Jump A
if Acc = 0: Jump A
Acc = C
Sub B
A = RAM[C]
B = RAM[Acc]
RAM[Acc] = A
RAM[C] = B
C = 5 # Num Data Points here
Acc = C # Label 2 here
B = 1
Sub B
C = Acc
Acc = 6 # Jump 1 Address # 1 + Num data Points
if C > 0: Jump Acc # Jump 1
Acc = 4 # Num data Points (-1)
A = RAM[Acc]
Out A
Sub B
C = 29 # Jump 2 Address Num data Points + 24
if Acc > 0: Jump C
if Acc = 0: Jump C
STOP