from itertools import permutations
from day5 import day5, parseFile
import math
def day7():
    max = -math.inf
    combination = None
    for each in permutations([0,1,2,3,4]):
        second_instruction = 0
        for amplifier in each:
            first_instruction = amplifier
            second_instruction = day5(parseFile('day7.txt'),[first_instruction,second_instruction])
            if amplifier == each[-1] and second_instruction > max:
                max = second_instruction
                combination = each

    print(max,flush=True)
    print(combination,flush=True)
    return
def main():
    day7()
    return
if __name__ == "__main__":
    main()
