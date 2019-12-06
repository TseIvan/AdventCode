import copy

OP_ADD = 1
OP_MUL = 2
OP_END = 99
def opcodeProgram(x,y,opcode) -> list:
    opcode = copy.deepcopy(opcode)
    opcode[1], opcode[2] = x,y
    index = 0
    # Now, your ship computer will also need to handle parameters in mode 1, immediate mode.
    # In immediate mode, a parameter is interpreted as a value - if the parameter is 50, its value is simply 50

    # Parameter modes are single digits, one per parameter, read right-to-left from the opcode: the first parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit,
    # the third parameter's mode is in the ten-thousands digit, and so on. Any missing modes are 0.
    # ABCDE
    # 01002
    # 1101 -> add instruction
    # DE- 2 digit op code
    # C - position mode
    # B - Immediate mode
    # A - position mode

    # opcode 1 = add, opcode 2 = multiply
    # 01002,4,3,4,33 -> immediate mode

    # multiply position 4(33) and position 3 -> 33*3 == 99 writes in 4 - > 1002,4,3,4,99

    # Because of the new instructions, this amount is no longer always 4.
    # Parameters that an instruction writes to will never be in immediate mode.

    # Not always increase index by 4

    # 1101,100,-1,4,0
    # 100 + (-1) -> store in pos 4: 1101,100,-1,4,-100






    # while (opcode[index] != 99):
    #     if opcode[index] == 1:
    #         opcode[opcode[index+3]] = opcode[opcode[index+1]] + opcode[opcode[index+2]]
    #     elif opcode[index] == 2:
    #         opcode[opcode[index+3]] = opcode[opcode[index+1]] * opcode[opcode[index+2]]
    #     elif opcode[index] == 3:
    #         pass
    #     elif opcode[index] == 4:
    #         pass

        index += 4
    return opcode

def day5(f1="day2.txt", p2 = False):
    with open(f1, 'r') as fp:
        text_from_file = fp.readlines()
    opcode = []
    for line in text_from_file:
        for char in line.rstrip('\n').split(","):
            if char.isdigit():
                opcode.append(int(char))

def main():
    print(day5())
    return 0


if __name__ == "__main__":
    main()
