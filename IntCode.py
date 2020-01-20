import copy
import sys
import math
# sys.maxsize

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

        self.programCopy = copy.deepcopy(program) # List
        self.program = copy.deepcopy(program) # List
        self.index = 0
        self.input = []
        self.output = []
        self.terminate = False
        self.relative_base = 0
    # day15 avoids backtracking
    def duplicate(self):
        dupe = IntCode(self.programCopy)
        dupe.index = self.index
        dupe.input = self.input
        dupe.output = self.output
        dupe.terminate = self.terminate
        dupe.relative_base = self.relative_base
        return dupe

    def input_signal(self,input):
        self.input.append(input)
        self.compile()

    def addMemory(self):
        self.program += 10**4 * [0] # This actually worked LOL

    def decompose(self,instruct,operation):
        instruct = [int(x) for x in str(instruct)]
        param_modes = ((5-len(instruct)) * [0]) + instruct

        # need to modify 1,2,7,8 all require 3 params
        # 5,6 only requires 2 params
        # 3,4,9 requires 1 param
        # we can avoid index errors like this

        first,second,third = None,None,None

        if param_modes[2] == 0:
            first = self.program[self.index + 1]
        elif param_modes[2] == 1:
            first = self.index + 1
        elif param_modes[2] == 2:
            first = self.program[self.index + 1] + self.relative_base

        if operation not in [3,4,9]:

            if param_modes[1] == 0:
                second = self.program[self.index + 2]
            elif param_modes[1] == 1:
                second = self.index + 2
            elif param_modes[1] == 2:
                second = self.program[self.index + 2] + self.relative_base

        if operation in [1,2,7,8]:

            if param_modes[0] == 0:
                third = self.program[self.index + 3]
            elif param_modes[0] == 1:
                third = self.index + 3
            elif param_modes[0] == 2:
                third = self.program[self.index + 3] + self.relative_base

        return {'first':first,'second':second,'third':third}

    def modifyIndex(self,operation,boolean):
        if operation in [1,2,7,8]:
            self.index += 4
        elif operation in [5,6]:
            if not boolean:
                self.index += 3
        elif operation in [3,4,9]:
            self.index += 2
        return

    def compile(self):
        self.addMemory() # Remove for day7
        while (self.index < len(self.program)):
            boolean = True
            instruct = self.program[self.index]
            operation = int(str(instruct)[-2:])
            if operation == 99: # Check op 99 before decompose or it will index error out.
                self.terminate = True
                return
            params = self.decompose(instruct,operation)
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
            elif operation == 9: # Move index >> 2
                self.relative_base += self.program[params.get('first')]
            self.modifyIndex(operation,boolean)

def main():

    return

if __name__ == "__main__":
    main()
