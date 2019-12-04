def computePoss(x:int = 206938,y:int = 679128) -> int:
    # 206938-679128 was my key
    # It is a six-digit number.
    # The value is within the range given in your puzzle input.
    # Two adjacent digits are the same (like 22 in 122345).
    # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

    counter = 0
    for number in range(x, y+1):
        if len(set(str(number))) <= 5: # Since there could be possibliity of being adjacent in any of the 6 positions we know that it set would have len <= 5
            if number == int("".join(sorted(str(number)))): # Left to right it must never decrease. eg 577999 has set len = 3 sorted it would be 5,7,7,9,9,9 and is within bounds
                print(number)
                counter += 1
    return counter

def repeatingSeq(number):
    # Every number is ensured a adjacent number
    dupe = set([x for x in str(number) if str(number).count(x) >= 2])
    if len(dupe) == 1:
        if str(number).count(next(iter(dupe))) == 2:
            return True
        return False # Only one repeating and it repeats more than twice
    else:
        for i in dupe:
            if str(number).count(i) == 2:
                return True
        return False

def changedCriteria(x:int = 206938,y:int = 679128) -> int:
    counter = 0
    for number in range(x, y+1):
        if len(set(str(number))) <= 5: # Since there could be possibliity of being adjacent in any of the 6 positions we know that it set would have len <= 5
            if number == int("".join(sorted(str(number)))): # Left to right it must never decrease. eg 577999 has set len = 3 sorted it would be 5,7,7,9,9,9 and is within bounds
                if repeatingSeq(int(number)):
                    counter += 1
    return counter

def main():
    print(changedCriteria())
    # print(repeatingSeq(666668))
    # print(repeatingSeq(123444))
    # print(repeatingSeq(112233))

    return
if __name__ == "__main__":
    main()
