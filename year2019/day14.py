# 9 ORE => 2 A
# 8 ORE => 3 B
# 7 ORE => 5 C
# 3 A, 4 B => 1 AB
# 5 B, 7 C => 1 BC
# 4 C, 1 A => 1 CA
# 2 AB, 3 BC, 4 CA => 1 FUEL
#
# 4CA = 4*4 C + 4*1A
# 3BC = 15B + 21C
# 2AB = 6A + 8B
#
# total = 10A + 23B + 37C
#
# 10 = 4*9 = 45
# 8*8 = 64
# 40/5 = 56
#
# 45+64+56 = 165

with open("day14.txt", 'r') as fp:
    chemical_dict = {}
    for line in fp.readlines():
        input,output = line.strip().split(' => ')

# TODO: Turn this into queue. Start with fuel, enqueue everything, pop off queue then add next ingredient, repeat until queue contains only ore, sum ore = win
