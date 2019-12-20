import re,copy,math

class Moon:
    def __init__(self,pos):
        self.pos = copy.deepcopy(pos)
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.z = self.pos[2]
        self.velo_x = 0
        self.velo_y = 0
        self.velo_z = 0
        self.initial = [self.pos[0],self.pos[1],self.pos[2]]
        self.repeat = False
        self.steps = 0
    def __str__(self):
        return "<%s,%s,%s> <%s,%s,%s>" % (self.x,self.y,self.z,self.velo_x,self.velo_y,self.velo_z)

    def getXYZ(self):
        return [self.x,self.y,self.z]

    def compute_gravity(self,other):
        if self.x != other[0]:
            self.velo_x = self.velo_x-1 if self.x > other[0] else self.velo_x+1
        if self.y != other[1]:
            self.velo_y = self.velo_y-1 if self.y > other[1] else self.velo_y+1
        if self.z != other[2]:
            self.velo_z = self.velo_z-1 if self.z > other[2] else self.velo_z+1
    def repeating(self,axis):
        if axis == 1:
            return self.x == self.initial[0] and [self.velo_x] == [0]
        elif axis == 2:
            return self.y == self.initial[1] and [self.velo_y] == [0]
        else:
            return self.z == self.initial[2] and [self.velo_z] == [0]

    def update(self,axis):
        self.x += self.velo_x
        self.y += self.velo_y
        self.z += self.velo_z
        if self.repeat != True:
            self.steps += 1
        if self.repeating(axis):
            self.repeat = True
    def reset(self):
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.z = self.pos[2]
        self.velo_x = 0
        self.velo_y = 0
        self.velo_z = 0
        self.initial = [self.pos[0],self.pos[1],self.pos[2]]
        self.repeat = False
        self.steps = 0

    def compute_energy(self):
        return sum([abs(self.x),abs(self.y),abs(self.z)]) * sum([abs(self.velo_x),abs(self.velo_y),abs(self.velo_z)])
def LCM(a,b):
    return a*b//math.gcd(a,b)

def main():
    Moons = []
    with open("day12.txt", 'r') as fp:
        for _ in [list(map(int,re.findall("[-?\d+]+",line))) for line in fp.readlines()]:
            Moons.append(Moon(_))
    max_steps = []
    for a in range(3):
        while(all([x.repeat for x in Moons]) != True):
            for x in Moons:
                for y in Moons:
                    if x!=y:
                        x.compute_gravity(y.getXYZ())
            for z in Moons:
                z.update(a)

        print([m.steps for m in Moons])
        max_steps.append(max(m.steps for m in Moons))
        [m.reset() for m in Moons]
    # print(max_steps)
    # [27253, 186028, 28482]
    print(LCM(LCM(max_steps[0],max_steps[1]),max_steps[2]))
    # for _ in range(1000):
    #     for x in Moons:
    #         for y in Moons:
    #             if x!=y:
    #                 x.compute_gravity(y.getXYZ())
    #     for z in Moons:
    #         z.update(0)
    # print(sum(p.compute_energy() for p in Moons))
    return
if __name__ == "__main__":
    main()
