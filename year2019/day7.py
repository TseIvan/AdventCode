from itertools import permutations
from day5 import day5, parseFile
import math
def day7()-> None:
    max = -math.inf
    combination = None
    for each in permutations(range(5)):
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
def day7part2()-> None:
    # Each amplifier needs phase setting (5,9) and input signal
    # Only halts on E.Amplifier == 99
    max = -math.inf
    initial = 0
    sequence = [9,8,7,6,5] #range(5,10)
    output = None

    return None
def main():
    # day7()
    day7part2()
    return
if __name__ == "__main__":
    main()
