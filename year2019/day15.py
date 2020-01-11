from IntCode import IntCode, parseFile
import heapq
import copy
dir_dict = {
    'north': {'change':[0,1], 'input':1},
    'south': {'change':[0,-1], 'input':2},
    'west': {'change':[-1,0], 'input':3},
    'east': {'change':[1,0], 'input':4},
}
def updatePos(x,y,dir):
    global dir_dict
    x += dir_dict[dir].get('change')[0]
    y += dir_dict[dir].get('change')[1]
    return (x,y)

def run():
    global dir_dict
    # directions = ['north','south','west','east']

    visited = {(0,0):" "}
    program = IntCode(parseFile('day15.txt'))
    # Initialize heap to store list
    h = list()
    heapq.heapify(h)

    # Storage structure -> list [tuple(int x,int y) , class:IntCode program, steps:int, direction:str]
    # Initialize start
    [heapq.heappush(h,[updatePos(0,0,dir),program,0,dir]) for dir in dir_dict.keys()]

    while len(h):
        (x,y),prog,steps,dir = heapq.heappop(h)
        dupe = prog.duplicate() # Create new duplicated instance
        dupe.input_signal(dir_dict[dir].get('input'))
        status = dupe.output.pop(0)
        # print(x,y,status,dir)
        if status == 2:
            visited[(x,y)] = "X"
            print(steps)
            return(steps)
        elif status == 1:
        #     print(x,y,status,dir)
            visited[(x,y)] = " "
            for dir in dir_dict.keys():
                x,y = updatePos(x,y,dir)
                if (x,y) not in visited.keys():
                    heapq.heappush(h,[(x,y),dupe.duplicate(),steps+1,dir])
        elif status == 0:
            visited[(x,y)] = "█"

run()
