class Asteroid:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.max = 0

    def __str__(self):
        return "x_coordinate %s, y_coordinate %s" %(self.x,self.y)



def uniqueSlope() -> bool:

    return False

with open("day10.txt", 'r') as fp:
    galaxy = fp.readlines()

    ast_list = []

    for x,line in enumerate(galaxy):
        for y,ast in enumerate(line):
            if ast == '#':
                ast_list.append(Asteroid(x,y))


# # TODO: figure out how to stack into matrix
# TODO: Find all the planets with hash mark, put it in dictionary
# Compute slope for each one (super bad time complexity)
#
