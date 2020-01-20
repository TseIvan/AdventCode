def day1(f1='day1.txt',p2 = False):
    with open(f1, 'r') as fp:
        text_from_file = fp.readlines()
    summation = 0
    for line in text_from_file:
        if isinstance(int(line), int):
            if (p2):
                n = int(line)
                while (True):
                    n = (n//3 -2)
                    if (n < 0):
                        break
                    else:
                        summation += n
            else:
                summation += (int(line)//3 -2)
    return summation

def main():
    print(day1())

    return
if __name__ == "__main__":
    main()
