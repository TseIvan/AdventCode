from anytree import Node, RenderTree, AsciiStyle, LevelOrderIter, Walker, find, findall
# python library anytree: https://pypi.org/project/anytree/
# Trying out anytree for fun, alternative is to write own Tree Struct
# Documentation - https://anytree.readthedocs.io/en/latest/#


# Possibility to map into dictionary then perform BFS for returning depth
# YOU and SAN are considered "terminating" would performance be bad? Should be O(N) of dictionary
# We know that COM is initial center of mass start state
global_counter = 0
def day6(f1:str="day6.txt"):
    orbit_list = [line.split(')') for line in open(f1, 'r').read().split('\n')]
    tracking = {}

    orbit_dict = {}
    for planet in orbit_list:
        if len(planet) == 2:
            # Trying out dictionary method + BFS
            if planet[0] not in tracking and planet[1] not in tracking:
                x = Node(planet[0])
                y = Node(planet[1], parent=x)
                tracking[planet[0]] = x
                tracking[planet[1]] = y
            elif planet[0] not in tracking and planet[1] in tracking:
                x = Node(planet[0])
                tracking[planet[0]] = x
                tracking[planet[1]].parent = x
            elif planet[0] in tracking and planet[1] not in tracking:
                x = Node(planet[1], parent=tracking[planet[0]])
                tracking[planet[1]] = x
            else:
                tracking[planet[1]].parent = tracking[planet[0]]

    indirect_orbit = 0
    for k,v in tracking.items():
        indirect_orbit += len(v.ancestors)
    print(indirect_orbit)

    # Use symmetric difference for minimum commonality
    # santa = set(tracking['SAN'].ancestors)
    # you = set(tracking['YOU'].ancestors)
    # print(len(santa^you))

    return

def indirect_orbit(d:dict,initial:list = ['COM'],counter:int = 0) -> int:
    global global_counter
    global_counter += counter*len(initial)
    for planet in initial:
        if planet in d:
            indirect_orbit(d,d[planet],counter+1)

def day6_alternative(f1:str="day6.txt"):
    orbit_list = [line.split(')') for line in open(f1, 'r').read().split('\n')]
    orbit_dict = {}
    for planet in orbit_list:
        if len(planet) == 2:
            if planet[0] not in orbit_dict:
                orbit_dict[planet[0]] = [planet[1]]
            else:
                orbit_dict[planet[0]].append(planet[1])

    # Loop through all planets connected to that until depth recursion.
    indirect_orbit(orbit_dict,counter=0)
    print(global_counter)

def main():
    day6()
    day6_alternative()
    return
if __name__ == "__main__":
    main()
