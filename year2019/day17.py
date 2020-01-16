from IntCode import IntCode, parseFile

def run():
    image = [[' ' for x in range(47)] for y in range(47)]
    program = IntCode(parseFile('day17.txt'))
    program.compile()

    x=y=0
    for char in program.output:
        if char == 35:
            image[x][y] = "#"
            x+=1
        elif char == 46:
            image[x][y] = "."
            x+=1
        elif char == 10:
            print("\n")
            y+=1
            x=0
    for line in image:
        print("".join(line))
    sum = 0
    for x in range(47):
        for y in range(47):
            try:
                if (image[x][y] == "#" and image[x+1][y] == "#" and image[x-1][y] == "#" and image[x][y+1] == "#" and image[x][y-1] == "#"):
                    sum += x*y
            except(IndexError):
                pass
    print(sum)
    return

run()
