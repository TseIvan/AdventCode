
def day1(f1='adventcode.txt',p2 = False):
    with open(f1, 'r') as fp:
        text_from_file = fp.readlines()
    summation = 0
    for line in text_from_file:
        if isinstance(int(line), int):
            if (p2):
                n = int(line)
                while (True):
                    n = (n//3 -2)
                    if (n < 0):
                        break
                    else:
                        summation += n
            else:
                summation += (int(line)//3 -2)
    return summation

def opcodeProgram(opcode) -> list:
    # Opcode 1 = Add, retrieve(index) and retrieve(index), add to pos at index+3
    # Opcode 2 = Multiplies, retrieve(index) and retrieve(index), add to pos at index+3
    # Opcode 99 = Halt
    # Rest = something went wrong
    index = 0
    while (index <= len(opcode) and opcode[index] != 99):
        if opcode[index] == 1:
            opcode[opcode[index+3]] = opcode[opcode[index+1]] + opcode[opcode[index+2]]
        elif opcode[index] == 2:
            opcode[opcode[index+3]] = opcode[opcode[index+1]] * opcode[opcode[index+2]]
        index += 4
    return opcode

def day2part1(f1="day2.txt"):
    # print(opcodeProgram([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50])
    # print(opcodeProgram([1,0,0,0,99]) == [2,0,0,0,99])
    # print(opcodeProgram([2,3,0,3,99]) == [2,3,0,6,99])
    # print(opcodeProgram([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
    # print(opcodeProgram([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])
    with open(f1, 'r') as fp:
        text_from_file = fp.readlines()
    opcode = []
    for line in text_from_file:
        for char in line.rstrip('\n').split(","):
            if char.isdigit():
                opcode.append(int(char))
    # #To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?
    opcode[1], opcode[2] = 12,2
    return opcodeProgram(opcode)[0]

def main():
    # print(day1())
    # print(day1(p2 = True))
    # print(day2part1())
    return 0


if __name__ == "__main__":
    main()
