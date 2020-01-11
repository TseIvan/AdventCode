from IntCode import IntCode, parseFile
import heapq
import copy

def run():
    dir_dict = {
        'north': {'change':[0,1], 'input':1},
        'south': {'change':[0,-1], 'input':2},
        'west': {'change':[-1,0], 'input':3},
        'east': {'change':[1,0], 'input':4},
    }
    # directions = ['north','south','west','east']

    visited = {(0,0):"█"}
    program = IntCode(parseFile('day13.txt'))
    # Initialize heap to store list
    h = list()
    heapq.heapify(h)

    # Storage structure -> list [tuple(int x,int y) , class:IntCode program, steps:int, direction:str]
    # Initialize start
    [heapq.heappush(h,[(0,0),program,0,dir]) for dir in dir_dict.keys()]

    while len(h):
         # north (1), south (2), west (3), and east (4)
        (x,y),prog,steps,dir = heapq.heappop(h)
        print((x,y))
        print(prog)
        print(steps)
        print(dir)
        dupe = program.duplicate() # Create new duplicated instance
        print(dir_dict[dir].get('input'))
        # dupe.input(dir_dict[dir].get('input'))
    return

run()
