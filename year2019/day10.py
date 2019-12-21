import numpy as np
from collections import defaultdict
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
        self.distance = -math.inf

    def __str__(self):
        return "x_coordinate %s, y_coordinate %s" %(self.x,self.y)

    def slope(self,other):
        angle = math.atan2((self.y - other.y),(self.x - other.x))
        self.unique.add(angle)
        return angle

    def set_max(self):
        self.max = len(self.unique)
        return
    def L2_norm(self,other):
        math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
        return

with open("day10.txt", 'r') as fp:
    galaxy = fp.readlines()

    ast_list = []

    for x,line in enumerate(galaxy):
        for y,ast in enumerate(line):
            if ast == '#':
                ast_list.append(Asteroid(x,y))

station = None
detected = -math.inf

for ast in ast_list:
    for other in ast_list:
        if ast != other:
            angle = ast.slope(other)

    ast.set_max()
    if ast.max > detected:
        detected = ast.max
        station = ast

print(detected) # 299
print(station) # x_coordinate 29, y_coordinate 26

ast_dict = defaultdict(list)

for other in ast_list:
    if other != station:
        station.L2_norm(other)
        angle = other.slope(station)
        ast_dict[angle].append(other)

for key in sorted(ast_dict.keys()):
    print(key, ast_dict[key][0])
    pass
# Compute atan2 for North east south west of the point 29,26

print(math.atan2((35 - 26),(30 - 29))) # North of point
# print(math.atan2((26 - 26),(29 - 30))) # East of point
# print(math.atan2((26 - 25),(29 - 29))) # South of point
# print(math.atan2((26 - 26),(29 - 28))) # West of point

# -3.107123552590285 x_coordinate 0, y_coordinate 25
# -1.5253730473733196 x_coordinate 30, y_coordinate 4
# 0.0 x_coordinate 37, y_coordinate 26
# 1.5707963267948966 x_coordinate 29, y_coordinate 29
# 3.141592653589793 x_coordinate 0, y_coordinate 26

# What if we put into "bins" and sort each "bin" (from pi/2 to 2pi)
