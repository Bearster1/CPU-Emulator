# CPU-Emulator
This is an emulator for a Custom CPU
Key Notes:
    When it says [REGISTER_NAME] you replace that with any of the four registers A, B, C, Acc.
        The Acc register is the left hand operand of any calculation you try to do.
    When it says [VALUE] you replace that with any number you require.
        You can also replace it with a letter encased in " and it will be replaced with it's ascii value.
            If you do "\n" it will be replaced with a new line.
        You can also replace it with a label name - see [NAME].
    When it says [FILE_NAME] you replace that with the file name the macro refers to.
    When it says [NAME] you replace that with the name of the label.
    All commands are case-insensitive.
    When there is a tab in this file it likely means it is an extention of the thing under it.
    To do a comment use a # and everything after will be a comment.

The Commands:
    0: Data [VALUE]
    1: [REGISTER_NAME] = [VALUE]
    2: [REGISTER_NAME] = RAM[VALUE]
    3: RAM[VALUE] = [REGISTER_NAME]
    4: [REGISTER_NAME] = [REGISTER_NAME]
    5: Add [REGISTER_NAME]
    6: Sub [REGISTER_NAME]
    7: Negate
    8: NAND [REGISTER_NAME]
    9: [REGISTER_NAME] = RAM[[REGISTER_NAME]]
    10: RAM[[REGISTER_NAME]] = [REGISTER_NAME]
    11: [REGISTER_NAME] = _[REGISTER_NAME] << | >> [VALUE]
        For this unlike others the data must be 1 nibble long which is the amount it shifts the value in the register by.
        Replace << | >> with whichever shift you want to do << for left shift, >> for right shift
    12: if [REGISTER_NAME] < 0: Jump [REGISTER_NAME]
    13: if [REGISTER_NAME] = 0: Jump [REGISTER_NAME]
    14: if [REGISTER_NAME] > 0: Jump [REGISTER_NAME]
    15: STOP
    16: In [REGISTER_NAME]
        This lets you enter a number or a letter.
        To enter a letter encase it in " then it converts to Ascii.
    17: Out Num [REGISTER_NAME]
        This outputs the number in the register
    18: Out [REGISTER_NAME]
        This outputs the letter from the ascii code in the register
    19: Macro [FILE_NAME]
    20: Label [NAME]