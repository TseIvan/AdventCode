import copy

input_instruction = 1

def decompose(opcode,instr,index):
    index = copy.deepcopy(index)
    str_instr = str(instr)
    parameter_modes = ([0]*(5-len(str_instr))) + list(str_instr) # [0, '1', '0', '0', '2']
    print(parameter_modes)
    print(parameter_modes[0])
    print(parameter_modes[1])
    print(parameter_modes[2])
    print(opcode[index+3])
    # ABCDE
    # C - mode of 1st parameter,  0 == position mode
    # B - mode of 2nd parameter,  1 == immediate mode
    # A - mode of 3rd parameter,  0 == position mode

    # if parameter_modes[3] == 0:
    #     val_1 = 0
    # else:
    #     val_1 = opcode[index+1]
    # if parameter_modes[1] == 0:
    #     val_2 = 0
    # else:
    #     val_2 = opcode[index+2]
    # # if parameter_modes[0] == 0:
    # #     addr = 0
    # # else:
    # #     addr = opcode[index+3]
    # (opcode[idx + 3] if int(paramter_modes          [0]) == 0 else (idx + 3))
    print(addr)
    return {'first_param':val_1,'second_param':val_2,'addr':addr}

def opcodeProgram(opcode) -> list:

    index = 0
    while index < len(opcode):
        instr = opcode[index]
        op = int(str(instr)[-2:])
        params = decompose(opcode,instr,index)

        if op == 1:
            opcode[params.get('addr')] = opcode[params.get('first_param')] + opcode[params.get('second_param')]
            index += 4
        elif op == 2:
            opcode[params.get('addr')] = opcode[params.get('first_param')] * opcode[params.get('second_param')]
            index += 4
        elif op == 3:
            index += 4
        elif op == 4 or opcode == 99:
            break

        index += 5
    print(opcode)
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
