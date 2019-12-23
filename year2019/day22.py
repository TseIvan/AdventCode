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
