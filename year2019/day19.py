from IntCode import IntCode, parseFile
def run():
    sum = 0
    image=[[' ' for x in range(50)] for y in range(50)]
    for x in range(50):
        for y in range(50):
            program = IntCode(parseFile('day19.txt'))
            program.input_signal(x)
            program.input_signal(y)
            if program.output[-1] == 1:
                image[x][y] = "#"
            sum += program.output[-1]
    for line in image:
        print("".join(line))
    print(sum)
    return

def droneReport(x,y):
    program = IntCode(parseFile('day19.txt'))
    program.input_signal(x)
    program.input_signal(y)
    return program.output[-1]
def scan():
    # Relatively symmetric we can just check the top right corner and bottom left corner through brute force
    # checking (x,y) exists if (x,y+99) exist repeat for x+99
    x = y = 0
    while not droneReport(x, y+99):
        x += 1
        while not droneReport(x+99, y):
            y += 1
    # What value do you get if you take that point's X coordinate, multiply it by 10000, then add the point's Y coordinate?
    print(x*10000 + y)
    return
# run()
scan()
