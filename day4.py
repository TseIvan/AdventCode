def computePoss(x:int = 206938,y:int = 679128, p2:bool = False) -> int:
    # 206938-679128 was my key
    # It is a six-digit number.
    # The value is within the range given in your puzzle input.
    # Two adjacent digits are the same (like 22 in 122345).
    # Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

    counter = 0
    for number in range(x, y+1):
        if len(set(str(number))) <= 5: # Since there could be possibliity of being adjacent in any of the 6 positions we know that it set would have len <= 5
            if number == int("".join(sorted(str(number)))): # Left to right it must never decrease. eg 577999 has set len = 3 sorted it would be 5,7,7,9,9,9 and is within bounds. It's either already sorted or invalid
                if p2 and repeatingSeq(int(number)):
                    counter += 1
                elif not p2:
                    counter += 1
    return counter

def repeatingSeq(number):
    # Every number is ensured a adjacent number

    A = set([x for x in str(number) if str(number).count(x) == 2]) # Equal to 2
    B = set([x for x in str(number) if str(number).count(x) >= 3]) # Greater than 3
    # If it has len 1 then the value contained must not appear in greater than 3 len(A-B) = 0.
    # If the length of set A is greater than 1 then there are more than one possible adjacent characters, at minimum one of them has to not appear in greater than 3 len(B-A) != 0
    if (len(A-B) != 0 and len(A) == 1) or (len(A-B) != 0):
        return True
    return False

def main():
    print(computePoss())
    print(computePoss(p2=True))
    return
if __name__ == "__main__":
    main()
