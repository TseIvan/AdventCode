import copy


class IntCode:

    def __init__(self,program):
        self.program = copy.deepcopy(program) # List
        self.index = 0
        self.input = []
        self.output = []
        self.terminate = False

    def input_signal(self,input):
        self.input.append(input)

    def decompose(self,instruct):
        param_modes = ((5-len(instruct)) * [0]) + instruct
        first = self.index + 1 if param_modes[2] == 1 else self.program[self.index + 1] # if first param is a 1 then use immediate position, else retrieve the position at the index
        second = self.index + 2 if param_modes[1] == 1 else self.program[self.index + 2] # if second param is a 1 then use immediate position, else retrieve the position at the index
        third =  self.index + 3 if param_modes[0] == 1 else self.program[self.index + 3]
        return {'first':first,'second':second,'third':third}

    def modifyIndex(self,operation,boolean=False):
        if operation in [1,2,7,8]:
            self.index += 4
        elif operation in [5,6]:
            if not boolean:
                self.index += 3
        elif operation in [3,4]:
            self.index += 2
        return

    def compile(self):
        boolean = True
        instruct = self.program[self.index]
        operation = int(str(instruct)[-2:])
        params = self.decompose(instruct)
        while self.index < len(self.program):
            if instruct == 99:
                self.terminate = True
                return
            if instruct == 1:
                self.program[params.get('third')] = self.program[params.get('first')] + self.program[params.get('second')]

            elif instruct == 2:
                self.program[params.get('third')] = self.program[params.get('first')] * self.program[params.get('second')]
            elif instruct == 3:
                if len(self.input) == 0:
                    return
                self.program[params.get('first')] = self.input.pop(0)
            elif instruct == 4:
                self.output.append([params.get('first_param')])
            elif instruct == 5:
                if self.program[params.get('first')] != 0:
                    self.index = self.program[params.get('second')]
                else:
                    boolean = False
            elif instruct == 6:
            # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
                if self.program[params.get('first')] == 0:
                    self.index = self.program[params.get('second')]
                else:
                    boolean = False
            elif instruct == 7:
                self.program[params.get('third')] = int(self.program[params.get('first')] < self.program[params.get('second')])
            elif instruct == 8:
                self.program[params.get('third')] = int(self.program[params.get('first')] == self.program[params.get('second')])

            self.modifyIndex(operation,boolean)
            break


        return
