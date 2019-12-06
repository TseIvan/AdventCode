from anytree import Node, RenderTree, AsciiStyle, LevelOrderIter, Walker, find, findall
# python library anytree: https://pypi.org/project/anytree/
# Trying out anytree for fun, alternative is to write own Tree Struct
# Documentation - https://anytree.readthedocs.io/en/latest/#

def day7(f1:str="day7.txt", p2:bool = False):
    orbit_list = [line.split(')') for line in open(f1, 'r').read().split('\n')]
    tracking = {}
    for planet in orbit_list:
        if len(planet) == 2:
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
day7()
