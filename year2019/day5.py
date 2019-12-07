import copy

def opcodeProgram(opcode) -> list:
    return opcode

def day5(f1="day5.txt", p2 = False):
    with open(f1, 'r') as fp:
        text_from_file = fp.readlines()
    opcode = []
    for line in text_from_file:
        for char in line.rstrip('\n').split(","):
            if char.isdigit():
                opcode.append(int(char))

    opcodeProgram(opcode)
def main():
    day5()
    return 0


if __name__ == "__main__":
    main()
