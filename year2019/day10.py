import numpy as np
import math
# Cannot use Arctan eg 0,0 and -1,-1 rets 1. 0.0 and 1.1 rets 1. Both are the same
# Use atan2 to compute unique slopes https://en.wikipedia.org/wiki/Atan2
# atan2 takes y and x
class Asteroid:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.unique = set()
        self.max = -math.inf


    def __str__(self):
        return "x_coordinate %s, y_coordinate %s" %(self.x,self.y)

    def slope(self,other):
        self.unique.add(math.atan2((self.y - other.y),(self.x - other.x)))

    def set_max(self):
        self.max = len(self.unique)

with open("day10.txt", 'r') as fp:
    galaxy = fp.readlines()

    ast_list = []

    for x,line in enumerate(galaxy):
        for y,ast in enumerate(line):
            if ast == '#':
                ast_list.append(Asteroid(x,y))

for ast in ast_list:
    for other in ast_list:
        if ast != other:
            ast.slope(other)
    ast.set_max()

detected = -math.inf
for i in ast_list:
    if i.max > detected:
        detected = i.max
print(detected)

# # TODO: figure out how to stack into matrix
# TODO: Find all the planets with hash mark, put it in dictionary
# Compute slope for each one (super bad time complexity)
#
