from IntCode import IntCode, parseFile


def facing(original,direction):
    if original == 'west':
        new = 'south' if direction == 'left' else 'north'
    elif original == 'south':
        new = 'west' if direction == 'left' else 'east'
    elif original == 'east':
        new = 'north' if direction == 'left' else 'south'
    elif original == 'north':
        new = 'west' if direction == 'left' else 'east'
    return new

def run():

    init = [500,500]
    init_dir = 'north'

    dir_dict = {
        'north': [0,1],
        'west': [-1,0],
        'south':  [0,-1],
        'east': [1,0],
    }
    grid = [[0]*1000 for _ in range(1000)]
    twice = 0
    i = IntCode(parseFile('day11.txt'))
    while not i.terminate:
        color = grid[init[0]][init[1]]
        i.input_signal(color) # Pass color into put, either 0 or 1

        color_to_paint = i.output[-2]
        grid[init[0]][init[1]] = color_to_paint
        if color_to_paint == color:
            twice += 1
        direction = 'left' if i.output[-1] == 0  else 'right' # Direction to turn
        print(init)
        print(init_dir, direction)
        init_dir = facing(init_dir,direction)
        print(init_dir)
        init = [x + y for x, y in zip(init, dir_dict[init_dir])]
        print(init)
    return
run()
