from anytree import Node, RenderTree, AsciiStyle, LevelOrderIter, Walker, find, findall
from collections import defaultdict
# python library anytree: https://pypi.org/project/anytree/
# Trying out anytree for fun, alternative is to write own Tree Struct
# Documentation - https://anytree.readthedocs.io/en/latest/#


# Possibility to map into dictionary then perform BFS for returning depth
# YOU and SAN are considered "terminating" would performance be bad going through dictionary at most O(N) where N is length of textfile
# We know that COM is initial center of mass start state
global_counter = 0
san_set = set()
you_set = set()

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
    santa = set(tracking['SAN'].ancestors)
    you = set(tracking['YOU'].ancestors)
    print(len(santa^you))

    return

def indirect_orbit(d:dict,initial:list = ['COM'],counter:int = 0) -> None:
    global global_counter
    global_counter += counter*len(initial)
    for planet in initial:
        if planet in d:
            indirect_orbit(d,d[planet],counter+1)
def minimumCommonality(d,initial,a_set):
    for planet in initial:
        if planet in d:
            a_set.add(planet)
            minimumCommonality(d,d[planet],a_set)
    return

def day6_alternative(f1:str="day6.txt"):
    orbit_list = [line.split(')') for line in open(f1, 'r').read().split('\n')]
    orbit_dict = defaultdict(list)
    reverse_dict = defaultdict(list)
    print(orbit_dict)
    for planet in orbit_list:
        if len(planet) == 2:
            orbit_dict[planet[0]].append(planet[1])
            reverse_dict[planet[1]].append(planet[0])

    indirect_orbit(orbit_dict,counter = 0)
    print(global_counter)
    minimumCommonality(reverse_dict,['YOU'],you_set)
    minimumCommonality(reverse_dict,['SAN'],san_set)
    LCA = san_set^you_set
    LCA.discard('YOU')
    LCA.discard('SAN')
    print(len(LCA))

def main():
    # day6()
    day6_alternative()
    return
if __name__ == "__main__":
    main()
