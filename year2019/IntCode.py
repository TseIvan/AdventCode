import copy

def parseFile(f1:str="day5.txt")->list:
    with open(f1, 'r') as fp:
        text_from_file = fp.readlines()
    opcode = []
    for line in text_from_file:
        for char in line.split(","):
            opcode.append(int(char))
    return opcode

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
        instruct = [int(x) for x in str(instruct)]
        param_modes = ((5-len(instruct)) * [0]) + instruct
        first = self.index + 1 if param_modes[2] == 1 else self.program[self.index + 1] # if first param is a 1 then use immediate position, else retrieve the position at the index
        second = self.index + 2 if param_modes[1] == 1 else self.program[self.index + 2] # if second param is a 1 then use immediate position, else retrieve the position at the index
        third =  self.index + 3 if param_modes[0] == 1 else self.program[self.index + 3]
        return {'first':first,'second':second,'third':third}

    def modifyIndex(self,operation,boolean):
        if operation in [1,2,7,8]:
            self.index += 4
        elif operation in [5,6]:
            if not boolean:
                self.index += 3
        elif operation in [3,4]:
            self.index += 2
        return

    def compile(self):

        while (self.index < len(self.program)):
            boolean = True
            instruct = self.program[self.index]
            operation = int(str(instruct)[-2:])
            if operation == 99: # Check op 99 before decompose or it will index error out.
                self.terminate = True
                return
            params = self.decompose(instruct)
            if operation == 1:
                self.program[params.get('third')] = self.program[params.get('first')] + self.program[params.get('second')]
            elif operation == 2:
                self.program[params.get('third')] = self.program[params.get('first')] * self.program[params.get('second')]
            elif operation == 3:
                if len(self.input) == 0:
                    return
                self.program[params.get('first')] = self.input.pop(0)
            elif operation == 4:
                self.output.append(self.program[params.get('first')])
            elif operation == 5:
                if self.program[params.get('first')] != 0:
                    self.index = self.program[params.get('second')]
                else:
                    boolean = False
            elif operation == 6:
                if self.program[params.get('first')] == 0:
                    self.index = self.program[params.get('second')]
                else:
                    boolean = False
            elif operation == 7:
                self.program[params.get('third')] = int( self.program[params.get('first')] < self.program[params.get('second')])
            elif operation == 8:
                self.program[params.get('third')] = int( self.program[params.get('first')] == self.program[params.get('second')])

            self.modifyIndex(operation,boolean)

def main():
    
    return

if __name__ == "__main__":
    main()
