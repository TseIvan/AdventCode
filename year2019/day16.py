import numpy as np
import math

def compute_signal():
    with open("day16.txt", 'r') as fp:
        signal = np.array([int(x) for x in fp.read().rstrip('\n')])

    offset = int("".join([str(x) for x in (signal[:7]).tolist()]))
    repeat_pattern = [0, 1, 0, -1]
    offset_applied = False
    iter = 0
    while(iter < 10000):
        new_signal = []
        for i in range(signal.size): # Loops 8 times
            pattern = (np.repeat(repeat_pattern,i+1).tolist()) # Pattern shifted left by one
            pattern = np.array((pattern*math.ceil(signal.size/(len(pattern)-1)))[1:signal.size+1])
            new_signal.append(str(repr(np.sum(np.multiply(signal,pattern)))[-1]))

        if len(new_signal) > offset and offset_applied == False:
            offset_applied = True
            repeat_pattern = [0,0,1,0,-1]
            signal[offset:]
        else:
            signal = np.array([int(x) for x in new_signal])
        if iter%1000: # sanity check
            print("1000 Done",flush=True)
        iter += 1
    print(signal[:10],flush=True)
    return

compute_signal()
