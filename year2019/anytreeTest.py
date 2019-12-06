from anytree import Node, RenderTree, AsciiStyle, LevelOrderIter, Walker
# python library anytree: https://pypi.org/project/anytree/
# Could be done strictly using dictionary but I'm trying out anytree for fun visualization
# Documentation - https://anytree.readthedocs.io/en/latest/#

# udo = Node("Udo")
# marc = Node("Marc", parent=udo)
# lian = Node("Lian", parent=marc)
# dan = Node("Dan", parent=udo)
# jet = Node("Jet", parent=dan)
# jan = Node("Jan", parent=dan)
# joe = Node("Joe")
# udo.parent = joe
#
# for pre, fill, node in RenderTree(joe):
#     print("%s%s" % (pre, node.name))

def day7(f1="day7.txt", p2 = False):
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

day7()
