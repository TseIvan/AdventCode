from itertools import permutations
from day5 import day5, parseFile
from IntCode import IntCode
import math

def day7():
    max_signal = []
    for each in permutations(range(5)):
        second_instruction = 0
        for amplifier in each:
            first_instruction = amplifier
            prog = IntCode(parseFile('day7.txt'))
            prog.input_signal(first_instruction)
            prog.input_signal(second_instruction)
            second_instruction = prog.output[-1]
            max_signal.append(second_instruction)
    print(max(max_signal),flush=True)

def day7p2():
    max_signal = list()
    for each in permutations(range(5,10)):
        computers = [IntCode(parseFile('day7.txt')) for x in range(5)] # New Computers for each potential Sequence
        for index,comp in enumerate(computers):
            comp.input_signal(each[index]) # integers from 5 to 9, again each used exactly once
            if index == 0:
                comp.input_signal(0) # 0 signal is sent to amplifier A's input exactly once
        while not computers[4].terminate: # While Amplifier E is not 99 (Terminate = False)
            for index, comp in enumerate(computers):
                out = comp.output[-1]
                index = (index + 1) % 5 # Send output to next computer. If enum = 5 then send to computer first computer 0
                computers[index].input_signal(out)
                max_signal.append(out) # Store all output in max sig, at termination max_signal will contain a number that is greatest.  We dont need to care about Amp A-D because at best they will be <= Amp E output at term.
    print(max(max_signal))

def main():
    day7()
    day7p2()
    return
if __name__ == "__main__":
    main()
