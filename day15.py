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
    for dir in dir_dict.keys():
        heapq.heappush(h,[updatePos(0,0,dir),program,0,dir])

    while len(h):
         (x,y),prog,steps,dir = heapq.heappop(h)
         prog.input_signal(dir_dict[dir].get('input'))
         status = prog.output.pop(0)
         dupe = prog.duplicate() # Create new duplicated instance
         if status == 0:
             visited[(x,y)] = '█'
         elif status == 1:
             visited[(x,y)] = " "
             for dir in dir_dict.keys():
                 x,y = updatePos(x,y,dir)
                 if (x,y) not in visited.keys():
                     heapq.heappush(h,[(x,y),dupe,steps+1,dir])
         elif status == 2:
             visited[(x,y)] = "0"
             return(steps)




run()
