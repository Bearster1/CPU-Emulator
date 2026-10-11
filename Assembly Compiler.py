# TO DO:
# Now that macros are done do Labels
# LABELS

def base(line):
        if '0x' in line:
                line = int(line, 16)
        elif '0b' in line:
                line = int(line, 2)
        else:
                line = int(line)
        return line
def hexCode(value, size = 4):
        return hex(value).replace("0x", "").zfill(size)
def decodeLine(line, character, binaryFile, lineNum, labels, lines, macroPointer, usedMacros, macros):
        registers = ["a", "b", "c", "acc"]
        line = line.lower()
        if 'data' == line[:4]:
                line = line.replace('data', '')
                line = base(line)
        elif '=' in line and not 'if' == line[:2]:
                # print('a', line)
                destination, source = line.split('=')
                # print(destination, source)
                if destination in registers:
                        destination = registers.index(destination)
                        # print(destination)
                        immediate = False
                        try:
                                data = base(source)
                                immediate = True
                                # print('maybe', line)
                                # print(line)
                                line = base(hex(0x10 + destination) + hexCode(data, 2))
                                # print('It true', hex(line))
                        except Exception as e:
                                pass
                                # print('Fail', e)
                        # print(source, 2959)
                        if immediate:
                                pass
                        elif source in registers:
                                # print(935)
                                source = registers.index(source)
                                line = 0x4000 + (0b100 * source + destination) * 0x100
                        elif source[0] == "r":
                                source = source.replace(']', '[').split('[')[1]
                                try:
                                        data = base(source)
                                        line = 0x2000 + destination * 0x100 + data
                                        # print(line,2773)
                                except Exception as e:
                                        source = registers.index(source)
                                        line = 0x9000 + (destination + source*0b100) * 0x100
                        elif source[:5] == 'label':
                                # print(line)
                                shift = 0
                                if len(macros) > 0:
                                	macro = macros[len(macros)-1]
                                	shift = usedMacros[macro]
                                line = line + str(shift)
                                return line, lineNum, macroPointer
                        else:
                                # print(')×&;£', line, source)
                                if '>>' in line:
                                        source = source.split('>>')
                                        data = source[1]
                                else:
                                        source = source.split('<<')
                                        data = source[1] * 0b100
                                line = 0xB + destination + source[0] * 0b100 + data
                elif destination[0] == "r":
                        destination = destination.replace(']', '[').split('[')[1]
                        # print(destination, 3333)
                        source = registers.index(source)
                        try:
                                data = base(destination)
                                line = 0x3000 + source * 0b100 + data
                                # print(line,2773)
                        except Exception as e:

                                destination = registers.index(destination)

                                line = 0xA000 + (source + destination*0b100) * 0x100
        elif line[0:3] == "add":
                source = line.replace('add', '')
                source = registers.index(source)
                line = 0x5000 + source * 0b100 * 0x100
        elif line[0:3] == "sub":
                source = line.replace('sub', '')
                source = registers.index(source)
                line = 0x6000 + source * 0b100 * 0x100
        elif line == 'negate':
                line = 0x7000
        elif line[0:4] == 'nand':
                source = line.replace('nand', '')
                source = registers.index(source)
                line = 0x8000 + source * 0b100 * 0x100

        elif 'if' == line[:2]:
                line = line.replace('if', '').replace('0:jump', '')
                if '<' in line:
                        locations = line.split('<')
                        line = 0xC000
                elif '=' in line:
                        locations = line.split('=')
                        line = 0xD000
                elif '>' in line:
                        locations = line.split('>')
                        line = 0xE000
                source = registers.index(locations[0])
                destination = registers.index(locations[1])
                line += (source * 0b100 + destination) * 0x100
        elif 'in' == line[:2]:
                destination = registers.index(line.replace('in', ''))
                line = 0x0400 + destination * 0x100
        elif 'outnum' == line[:6]:
                destination = registers.index(line.replace('outnum', ''))
                line = 0x0800 + destination * 0x100
        elif 'out' == line[:3]:
                destination = registers.index(line.replace('out', ''))
                line = 0x0C00 + destination * 0x100
        elif 'macro' == line[0:5]:
                line = f"{line[5:]}.asm"
                # print(line, lineNum)
                if line in usedMacros:
                	usedMacros[line] += 1
                else:
                	usedMacros[line] = 1
                macros.append(line)
                macroPointer += 1
                lines, lineNum, macroPointer = writeFile(line, 'Programs/', binaryFile, lineNum, labels, lines, macroPointer, usedMacros, macros)
                macros.pop()
                macroPointer -= 1
                # print(line, lineNum)
                line = 0
                
                return line, lineNum, macroPointer
        elif 'label' == line[0:5]:
                shift = 0
                if len(macros) > 0:
                	macro = macros[len(macros)-1]
                	shift = usedMacros[macro]
                line = line[5:] + str( shift )
                labels[line] = lineNum
                line = 0
                # print(lineNum, labels)
                return line, lineNum, macroPointer
        elif line == "stop":
                line = 0xFFFF
        return hex(int(line)), lineNum, macroPointer
def readWriteFile(fileName, filePath):
        binaryFileName = 'Binary/'
        binaryFileName += fileName.replace('.asm', '.bin')
        with open(f"{filePath}/{fileName}", 'r') as file: # Stops it from making new files when they aren't needed.
                binaryFile = open(binaryFileName, 'w')
        labels = {}
        lines = []
        macroPointer = 0
        usedMacros = {}
        macros = []
        
        lines, lineNum, macroPointer = writeFile(fileName, filePath, binaryFile, 0, labels, lines, macroPointer, usedMacros, macros)
        i = 0
        # print(lines, labels)
        for line in lines:
                i += 1
                if "label" in line and line[0:5] != "label":
                        line = line.split("label")
                        line = line[0]+str(labels[line[1].lower()])
                        line, lineNum, macroPointer = decodeLine(line, None, binaryFile, None, labels, lines, macroPointer, usedMacros, macros)
                if i != len(lines):
                        line += '\n'
                # print(line)
                binaryFile.write(line)
        binaryFile.close()
        print("Program complied...")
def writeFile(fileName, filePath, binaryFile, lineNum, labels, lines, macroPointer, usedMacros, macros):
        with open(f"{filePath}/{fileName}", 'r') as file:
                for line in file:
                        character = None
                        if '"' in line:
                                letter = line.split('"')[1]
                                if letter == '\\n':
                                        character = 10
                                else:
                                        character = ord(letter)
                                line = line.replace(f'"{letter}"', str(character))
                                # print(line)

                        line = line.replace(' ', '').replace('\n', '')
                        if '#' in line:
                                comment = line.find('#')
                                line = line[0:comment]
                        if line == '':
                                continue
                        # print(line)
                        binaryLine, lineNum, macroPointer = decodeLine(line, character, binaryFile, lineNum, labels, lines, macroPointer, usedMacros, macros)
                        # print(binaryLine)

                        lineNum += 1

                        if binaryLine == None:
                                continue
                        lines.append(f"{binaryLine}")
        return lines, lineNum, macroPointer
def loadFile():
        fileName = input("Enter the name of the file that you would like to compile (Without extension - it is a .asm file): ")
        fileName += ".asm"
        readWriteFile(fileName, 'Programs/')

if __name__ == "__main__":
        loadFile()