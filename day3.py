import math
R = [1,0]
L = [-1,0]
D = [0,-1]
U = [0,1]
def manhattanDistance(x1:int, y1:int, x2:int, y2:int) -> int:
    # https://en.wikipedia.org/wiki/Taxicab_geometry
    # Argument as initial x,y followed by termination x,y
    return abs(x1 - x2) + abs(y1 - y2)

def parseFile(f1:str='day3.txt',p2 = False):
    with open(f1, 'r') as fp:
        text_from_file = fp.read()

    instructions = text_from_file.split("\n")

    return [i for i in instructions[0].split(",")] , [i for i in instructions[1].split(",")]

def intersection(coordinate_1:dict, coordinate_2:dict) -> list:
    
    return []

def smallestDistanceFromOrigin(coordinates:dict) -> int:
    minimumDistance = math.inf
    for coord in coordinates:
        distance = manhattanDistance(0,0,coord[0],coord[1])
        if (distance < minimumDistance):
            minimumDistance = distance
    return minimumDistance

def computeWire(direction:dict) -> list:
    init = [0,0]
    lineSegmentCoordinates = [init]
    for i in direction:
        if i[0] == "R":
            coord = [int(i[1:])*val for val in R]
        elif i[0] == "L":
            coord = [int(i[1:])*val for val in L]
        elif i[0] == "U":
            coord = [int(i[1:])*val for val in D]
        elif i[0] == "D":
            coord = [int(i[1:])*val for val in U]

        init = [x + y for x, y in zip(init, coord)]
        lineSegmentCoordinates.append(init)
    return lineSegmentCoordinates

def main():
    #What is the Manhattan distance from the central port to the closest intersection?
    # print(manhattanDistance(0,0,3,3),flush=True)
    # print(parseFile())

    # print(computeWire(parseFile()[0]))
    # print(computeWire(parseFile()[1]))




    return 1

if __name__ == "__main__":
    main()
