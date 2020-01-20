import re

def deal_with_increment(n,deck) -> list:
    new_stack = [0]*len(deck)
    i = 0
    for idx,val in enumerate(deck):
        new_stack[i] = val
        i = (i+n) % len(deck)
    return new_stack

def cut(n,deck) -> list:
    return deck[n:]+deck[:n]

def deal_into_new_stack(deck) ->list:
    return deck[::-1]

with open('day22.txt','r') as fp:
    deck = [i for i in range(0,10007)]
    for line in fp.readlines():
        line = line.strip()
        if line == "deal into new stack":
            deck = deal_into_new_stack(deck)
        elif line.split()[0] == "cut":
            deck = cut(int(line.split()[1]),deck)
        else:
            deck = deal_with_increment(int(line.split('deal with increment ')[1]),deck)

print(deck.index(2019))

# Part 2
# find card in position 2020
# deck = 119315717514047
# repeat = 101741582076661

# cut = (n + len(deck) + index) % len(deck)
# deal = len(deck) - 1 - i
# increment = modinverse(n,deck(len)) * index % len(deck)

# Algorithm for part 2 provided. Need to read more on sequences in modulo
# https://przybyl.io/solution-explanation-to-day-22-of-advent-of-code-2019.html
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)
#
# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('modular inverse does not exist')
#     else:
#         return x % m
