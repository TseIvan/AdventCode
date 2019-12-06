san_set = set()
you_set = set()
def day6_alternative(f1:str="day6.txt"):
    orbit_list = [line.split(')') for line in open(f1, 'r').read().split('\n')]
    reverse_dict = {}
    for planet in orbit_list:
        if len(planet) == 2:
            if planet[1] not in reverse_dict:
                reverse_dict[planet[1]] = [planet[0]]
            else:
                reverse_dict[planet[1]].append(planet[0])
    mc(reverse_dict,['YOU'],you_set)
    mc(reverse_dict,['SAN'],san_set)
    min = san_set^you_set
    min.discard('YOU')
    min.discard('SAN')
    print(len(min))
def mc(d,initial,a_set):
    global set
    for planet in initial:
        if planet in d:
            a_set.add(planet)
            mc(d,d[planet],a_set)
    return

def main():

    day6_alternative()

    return

if __name__ == "__main__":
    main()
# indirect_orbit(orbit_dict,counter=0)
#print(global_counter)
