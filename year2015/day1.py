
def parseFile(f1:str='day1.txt') -> int:
    with open(f1, 'r') as fp:
        text_from_file = fp.read().rstrip("\n")

    floor = 0
    for index,char in enumerate(text_from_file):
        if char == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print("basement at inedx: " + str(index + 1), flush = True)
    print(floor, flush = True)
    return floor

def main():
    parseFile()
    return

if __name__ == "__main__":
    main()
