C = 0x100 # Initialises the stack
In A
RAM[C] = A # Pushes A to the stack...
Acc = C
C = 1
Add C
C = Acc # ...Pushes A to the stack
Acc = C # Pops Stack to B...
C = 1
Sub C
C = Acc
B = RAM[C] # ...Pops Stack to B
Out num B