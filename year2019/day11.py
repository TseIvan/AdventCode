from IntCode import IntCode, parseFile
import matplotlib.pyplot as plt

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
    print(len(dict))
    return dict

def paint():
    dict = run(1)

    maxx = max(dict, key = lambda panel: panel[0])[0]
    minx = min(dict, key = lambda panel: panel[0])[0]

    xrange = maxx-minx+1 # end-start+1

    maxy = max(dict, key = lambda panel: panel[1])[1]
    miny = min(dict, key = lambda panel: panel[1])[1]

    yrange = maxy-miny+1

    grid = [[' ']*(yrange) for _ in range(xrange)]
    for k,v in dict.items():
        if v == 1:
            grid[k[0]-minx][k[1]-miny] = '█'
    [print(''.join(line)) for line in grid]

run(0)
paint()
