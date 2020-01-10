import sys
from IntCode import IntCode, parseFile


def facing(original,direction):
    if original == 'west': # West g
        new = 'south' if direction == 'left' else 'north'
    elif original == 'south': # South
        new = 'east' if direction == 'left' else 'west'
    elif original == 'east': # East
        new = 'north' if direction == 'left' else 'south'
    elif original == 'north': # North
        new = 'west' if direction == 'left' else 'east'
    return new

def run(color):
    init_dir = 'north'
    dir_dict = {
        'north': [0,1],
        'south':  [0,-1],
        'west': [-1,0],
        'east': [1,0],
    }
    x = y = 0
    dict = {(0,0):color}
    program = IntCode(parseFile('day11.txt'))
    while not program.terminate:
        program.input_signal(dict[(x,y)] if (x,y) in dict else 0) # 1 or 0
        dict[(x,y)] = program.output.pop(0)
        direction = 'left' if program.output.pop(0) == 0 else 'right'
        init_dir = facing(init_dir,direction)
        x = x + dir_dict[init_dir][0]
        y = y + dir_dict[init_dir][1]
    # print(len(dict))
    return dict

def paint():
    # eight capital letters.
    # Each Letter is 6x6
    dict = run(1)
    coord_list = [k for k,v in dict.items()]
    ones = coord_list = [k for k,v in dict.items() if v == 1]

    x_max = max(coord_list)[0]
    x_min = min(coord_list)[0]
    y_max = max(coord_list)[1]
    y_min = min(coord_list)[1]
    total = 0
    for y in range(y_min-2,y_max+2):
        for x in range(x_min-2,x_max+2):
            if (x,y) in dict:
                if (x,y) in ones:
                    print('X',end='')
                else:
                    print(' ',end='')
        print('\n')
# run(0)
paint()
