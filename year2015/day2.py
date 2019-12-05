import re
import numpy as np

def parseFile(f1:str='day2.txt',p2:bool=False) -> int:
    with open(f1, 'r') as fp:
        text_from_file = fp.readlines()

    total = 0
    for index,line in enumerate(text_from_file):
        dim = re.findall("\d+",line)# lwh
        dim = [int(x) for x in dim]
        calculation = [dim[0]*dim[1], dim[1]*dim[2], dim[0]*dim[2]]
        if p2:
            sorted_lwh = sorted(dim)
            total += 2*sorted_lwh[0] + 2*sorted_lwh[1] + np.prod(np.array(sorted_lwh))
        else:
            total += min(calculation) + sum(calculation) * 2
    print(total,flush=True)
    return total

def main():
    # 2*l*w + 2*w*h + 2*h*l
    parseFile(p2=True)
    return

if __name__ == "__main__":
    main()
