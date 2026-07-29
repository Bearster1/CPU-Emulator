data "H"
data "e"
data "l"
data "l"
data "o"
data " "
data "w"
data "o"
data "r"
data "l"
data "d"
data "!"
data "\n"
B = 12 # This is the number of letters
C = 1 # Jump here
A = RAM[Acc]
Out A
Add C
C = Acc
Acc = B
B = 1
Sub B
B = Acc
Acc = C
C = 14
if B > 0: Jump C