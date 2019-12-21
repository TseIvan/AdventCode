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

# Our grid is not cartesian plane
#  [0..............N]
#  [.               ]
#  [.               ]
#  [.               ]
#  [.               ]
#  [N               ]

# Fuck it convert to polar coordinates? And set x_coordinate 29, y_coordinate 26 as origin then sort by angle?
