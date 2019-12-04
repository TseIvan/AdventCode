import math
R = [1,0]
L = [-1,0]
D = [0,-1]
U = [0,1]
# Could improve code by figuring a better way to compute intersections and reusing code for computing line segments
def manhattanDistance(x1:int, y1:int, x2:int, y2:int) -> int:
    # https://en.wikipedia.org/wiki/Taxicab_geometry
    # Argument as initial x,y followed by termination x,y
    return abs(x1 - x2) + abs(y1 - y2)

def parseFile(f1:str='day3.txt',p2 = False):
    with open(f1, 'r') as fp:
        text_from_file = fp.read()

    instructions = text_from_file.split("\n")

    return [i for i in instructions[0].split(",")] , [i for i in instructions[1].split(",")]

def findIntersection(p1,p2,p3,p4):
    # Make a set for the line segment by inserting each point from x,y to x',y' into set, repeat for the second line segment. Any intersections can be computed using intersect function of sets
    # This will be beneficial incase of parallel lines
    line_segment = set()
    line_segment_2 = set()
    if p1[0] == p2[0]: # X axis same
        for y in range(min(p1[1],p2[1]),max(p1[1],p2[1])+1):
            line_segment.add((p1[0],y))

    if p1[1] == p2[1]:
        for x in range(min(p1[0],p2[0]),max(p1[0],p2[0])+1):
            line_segment.add((x,p1[1]))

    if p3[0] == p4[0]: # X axis same
        for y in range(min(p3[1],p4[1]),max(p3[1],p4[1])+1):
            line_segment_2.add((p3[0],y))

    if p3[1] == p4[1]:
        for x in range(min(p3[0],p4[0]),max(p3[0],p4[0])+1):
            line_segment_2.add((x,p3[1]))


    collision = line_segment.intersection(line_segment_2)
    collision.discard((0,0))

    return collision

def intersection(coordinate_1:dict, coordinate_2:dict) -> list:
    intersects = []
    for index_1,first_segment in enumerate(coordinate_1[:-1]):
        for index_2,second_segment in enumerate(coordinate_2[:-1]):
            p1 = (coordinate_1[index_1][0],coordinate_1[index_1][1])
            p2 = (coordinate_1[index_1+1][0],coordinate_1[index_1+1][1])

            p3 = (coordinate_2[index_2][0],coordinate_2[index_2][1])
            p4 = (coordinate_2[index_2+1][0],coordinate_2[index_2+1][1])

            set = findIntersection(p1,p2,p3,p4)
            if set != None:
                for i in set:
                    intersects.append(i)
    return intersects

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
            coord = [int(i[1:])*val for val in U]
        elif i[0] == "D":
            coord = [int(i[1:])*val for val in D]
        init = [x + y for x, y in zip(init, coord)]
        lineSegmentCoordinates.append(init)
    return lineSegmentCoordinates

def contains(p1,p2,x,y):
    p1 = p1.copy()
    p2 = p2.copy()
    line_segment = set()
    if p1[0] == p2[0]:
        for y in range(min(p1[1],p2[1]),max(p1[1],p2[1])+1):
            line_segment.add((p1[0],y))
    if p1[1] == p2[1]:
        for x in range(min(p1[0],p2[0]),max(p1[0],p2[0])+1):
            line_segment.add((x,p1[1]))
    line_segment.discard((0,0))
    return (x,y) in line_segment

def minimizer(coordinate_1:dict,collision:list):
    steps = 0
    for index,coord in enumerate(coordinate_1[:-1]):
        for col in collision:
            does_contains = contains(coordinate_1[index],coordinate_1[index+1],col[0],col[1]) # It either contains or it does not
            if does_contains:
                steps += manhattanDistance(coordinate_1[index][0],coordinate_1[index][1],col[0],col[1])
                return [steps, col[0],col[1]]
        steps += manhattanDistance(coordinate_1[index][0],coordinate_1[index][1],coordinate_1[index+1][0],coordinate_1[index+1][1])

def returnBestSolution():
    # NOTE: By following the steps in first set of instructions it will reach the first point of collision and calculate the steps taken
    # However this may not be the first collision point when using the second sets of instructions (potentially last step)
    # By retrieveing two points of collision we can figure out the amount of steps required to reach each point using both instructions
    # We know that the minimum of both will minimize the steps taken

    points_of_interect = intersection(computeWire(parseFile()[0]),computeWire(parseFile()[1]))
    results = minimizer(computeWire(parseFile()[0]),points_of_interect)
    sol_1 = results[0] + minimizer(computeWire(parseFile()[1]),[[results[1],results[2]]])[0]

    results = minimizer(computeWire(parseFile()[1]),points_of_interect)
    sol_2 = results[0] + minimizer(computeWire(parseFile()[0]),[[results[1],results[2]]])[0]
    return min(sol_1,sol_2)
def main():
    #What is the Manhattan distance from the central port to the closest intersection?
    # print(manhattanDistance(0,0,3,3),flush=True)
    print(returnBestSolution())
    # points_of_interect = intersection(computeWire(parseFile()[0]),computeWire(parseFile()[1]))
    # print(points_of_interect)
    # print(smallestDistanceFromOrigin(points_of_interect))

    # print(parseFile()[0])
    # print(computeWire(parseFile()[0]))
    # print(computeWire(parseFile()[1]))

    # print(smallestDistanceFromOrigin([[5,5],[10,10]]))
    # print(findIntersection(0,0,0,0,0,0,0,0))


    return 1

if __name__ == "__main__":
    main()
