import numpy as np
import math
from itertools import accumulate

# def compute_signal():
#     with open("day16.txt", 'r') as fp:
#         signal = np.array([int(x) for x in fp.read().rstrip('\n')])
#
#     offset = int("".join([str(x) for x in (signal[:7]).tolist()]))
#     repeat_pattern = [0, 1, 0, -1]
#     iter = 0
#     while(iter < 100):
#         new_signal = []
#         for i in range(signal.size): # Loops 8 times
#             pattern = (np.repeat(repeat_pattern,i+1).tolist()) # Pattern shifted left by one
#             pattern = np.array((pattern*math.ceil(signal.size/(len(pattern)-1)))[1:signal.size+1])
#             new_signal.append(str(repr(np.sum(np.multiply(signal,pattern)))[-1]))
#
#         signal = np.array([int(x) for x in new_signal])
#         iter += 1
#     print(signal)
#     return
def compute_signal_p2():
    with open("day16.txt", 'r') as fp:
        signal = [int(x) for x in fp.read().rstrip('\n')]*10000 # Signal repeated 10000 time
        offset = signal[:7]

    offset = int("".join(map(str, offset)))
    # https://work.njae.me.uk/2019/12/20/advent-of-code-2019-day-16/
    # Theory behind how to calculate provided ^
    # a+b+c+d+e+f = g = a+h
    #   b+c+d+e+f = h = b+i
    #     c+d+e+f = i = c+j
    #       d+e+f = j = d+k
    #         e+f = k = e+l
    #           f = l
    # Length of Signal = 6500000
    # Length of offset = 5976277
    # Difference = 523723 values we care about
    # We shift so far that we don't see negatives anymore only diagonlized 1s?
    signal = signal[offset:] # trunucate
    signal.reverse()
    for i in range(100):
        prev = 0
        new_signal = [0]*len(signal)
        for i in range(len(signal)):
            current = signal[i]
            new_signal[i] = (prev + signal[i])%10 # first iteration 0 + signal
            prev = new_signal[i]
        signal = new_signal
    signal.reverse()
    print("".join([str(x) for x in signal[:8]]))

compute_signal_p2()
