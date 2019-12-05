import copy

OP_ADD = 1
OP_MUL = 2
OP_END = 99
def opcodeProgram(x,y,opcode) -> list:
    # Opcode 1 = Add, retrieve(index) and retrieve(index), add to pos at index+3
    # Opcode 2 = Multiplies, retrieve(index) and retrieve(index), add to pos at index+3
    # Opcode 99 = Halt
    # Rest = something went wrong
    opcode = copy.deepcopy(opcode)
    opcode[1], opcode[2] = x,y
    index = 0
    while (opcode[index] != 99):
        if opcode[index] == 1:
            opcode[opcode[index+3]] = opcode[opcode[index+1]] + opcode[opcode[index+2]]
        elif opcode[index] == 2:
            opcode[opcode[index+3]] = opcode[opcode[index+1]] * opcode[opcode[index+2]]
        index += 4
    return opcode

def day2(f1="day2.txt", p2 = False):
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
    if not p2:
        return opcodeProgram(12,2,opcode)[0]
    # "With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to determine what pair of inputs produces the output 19690720."
    # Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)
    else:
        # while (opcodeProgram(opcode)[0] != 19690720):
        opcode = copy.deepcopy(opcode)
        for x in range(0,100):
            for y in range(0,100):
                if opcodeProgram(x,y,opcode)[0] == 19690720:
                    return 100 * x + y
        return -1

def main():
    # print(day1())
    # print(day1(p2 = True))
    print(day2())
    print(day2(p2 = True))
    return 0


if __name__ == "__main__":
    main()
