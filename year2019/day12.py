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
    def __str__(self):
        return "<%s,%s,%s> <%s,%s,%s>" % (self.x,self.y,self.z,self.velo_x,self.velo_y,self.velo_z)

    def getAxis(self,axis):
        if axis == 0: return self.x
        if axis == 1: return self.y
        if axis == 2: return self.z

    def getXYZ(self):
        return [self.x,self.y,self.z]

    def compute_gravity(self,other):
        if self.x != other[0]:
            self.velo_x = self.velo_x-1 if self.x > other[0] else self.velo_x+1
        if self.y != other[1]:
            self.velo_y = self.velo_y-1 if self.y > other[1] else self.velo_y+1
        if self.z != other[2]:
            self.velo_z = self.velo_z-1 if self.z > other[2] else self.velo_z+1

    def update(self,axis):
        self.x += self.velo_x
        self.y += self.velo_y
        self.z += self.velo_z

    def compute_energy(self):
        return sum([abs(self.x),abs(self.y),abs(self.z)]) * sum([abs(self.velo_x),abs(self.velo_y),abs(self.velo_z)])
def LCM(a,b):
    return a*b//math.gcd(a,b)
def compute_steps(Moons,mode):
    Moons = copy.deepcopy(Moons)
    axis_list = [moon.getAxis(mode) for moon in Moons]
    steps = 1
    while(True):
        steps += 1
        for x in Moons:
            for y in Moons:
                if x!=y:
                    x.compute_gravity(y.getXYZ())
        for z in Moons:
            z.update(mode)
        if axis_list == [moon.getAxis(mode) for moon in Moons]: break

    return steps

def main():
    Moons = []
    with open("day12.txt", 'r') as fp:
        for _ in [list(map(int,re.findall("[-?\d+]+",line))) for line in fp.readlines()]:
            Moons.append(Moon(_))

    # Part 2
    print(LCM(LCM(compute_steps(Moons,0),compute_steps(Moons,1)),compute_steps(Moons,2)))

    # Part 1
    for _ in range(1000):
        for x in Moons:
            for y in Moons:
                if x!=y:
                    x.compute_gravity(y.getXYZ())
        for z in Moons:
            z.update(0)
    print(sum(p.compute_energy() for p in Moons))
    return
if __name__ == "__main__":
    main()
