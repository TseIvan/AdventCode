import copy

def parseFile(f1:str="day5.txt")->list:
    with open(f1, 'r') as fp:
        text_from_file = fp.readlines()
    opcode = []
    for line in text_from_file:
        for char in line.split(","):
            opcode.append(int(char))
    return opcode

def decompose(opcode_list:list,instruct:int,index:int) -> dict:
    instruct = [int(x) for x in str(instruct)]
    # DE - two-digit opcode,      02 == opcode 2
    #  C - mode of 1st parameter,  0 == position mode
    #  B - mode of 2nd parameter,  1 == immediate mode
    #  A - mode of 3rd parameter,  0 == position mode
    param_modes = ((5-len(instruct)) * [0]) + instruct

    first = index + 1 if param_modes[2] == 1 else opcode_list[index + 1] # if first param is a 1 then use immediate position, else retrieve the position at the index
    second = index + 2 if param_modes[1] == 1 else opcode_list[index + 2] # if second param is a 1 then use immediate position, else retrieve the position at the index
    third =  opcode_list[index + 3] # Omitted

    return {'first_param':first,'second_param':second,'addr':third}

def day5(opcode_list:list = parseFile(),input_instruction:list=[5])->int:
    # print("-- Beginning New Run --")
    opcode_list = copy.deepcopy(opcode_list)
    input_instruction = copy.deepcopy(input_instruction)
    index = 0
    while index < len(opcode_list):
        instruct = opcode_list[index]
        operation = int(str(instruct)[-2:]) # Last two digits represent operation code
        params = decompose(opcode_list,instruct,index) # Decompose instruction based on immediate vs position mode
        if operation == 1: # add instruction increases index by 4
            opcode_list[params.get('addr')] = opcode_list[params.get('first_param')] + opcode_list[params.get('second_param')]
            index += 4
        elif operation == 2: # sub instruction increases index by 4
            opcode_list[params.get('addr')] = opcode_list[params.get('first_param')] * opcode_list[params.get('second_param')]
            index += 4
        elif operation == 3: # storage instruction increases index by 2
            opcode_list[params.get('first_param')] = input_instruction[0]
            input_instruction.pop(0)
            index += 2
        elif operation == 4: # print instruction increases index by 2
            if opcode_list[index+2] == 99: # Check two indexes ahead. When putting this in it's own elif decompose will reach IndexError.
                print("Operation Code 99, terminating. Final result = %s" % opcode_list[params.get('first_param')],flush=True)
                return opcode_list[params.get('first_param')]
                break
            else:
                print("Output Diagnostic Test %s" % opcode_list[params.get('first_param')] ,flush=True)
                return opcode_list[params.get('first_param')]
                index += 2
        elif operation == 5:
            if opcode_list[params.get('first_param')] != 0:
                index = opcode_list[params.get('second_param')]
            else:
                index += 3 # Instructions with 5 increment by 3 Instruct,first_param,second_param
        # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
        elif operation == 6:
            if opcode_list[params.get('first_param')] == 0:
                index = opcode_list[params.get('second_param')]
            else:
                index += 3 # Instructions with 5 increment by 3 Instruct,first_param,second_param

        # Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
        elif operation == 7:
            if opcode_list[params.get('first_param')] < opcode_list[params.get('second_param')]:
                opcode_list[params.get('addr')] = 1
            else:
                opcode_list[params.get('addr')] = 0
            index += 4
        # Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
        elif operation == 8:
            if opcode_list[params.get('first_param')] == opcode_list[params.get('second_param')]:
                opcode_list[params.get('addr')] = 1
            else:
                opcode_list[params.get('addr')] = 0
            index += 4

def main():
    day5()

if __name__ == "__main__":
    main()
