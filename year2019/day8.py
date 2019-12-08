

def main(f1:str="day8.txt") -> None:
    # 25 by 6
    with open(f1, 'r') as fp:
        text_from_file = list(fp.read().rstrip('\n'))

    layer = 25*6
    dictionary = {}
    for i in range(0,len(text_from_file),layer):
        partition = text_from_file[i:i+layer]
        dictionary["".join(partition)] = partition.count('0')


    lowest = min(dictionary,key=dictionary.get)
    print(int(lowest.count('1'))*int(lowest.count('2')),flush = True)
    
    return
if __name__ == "__main__":
    main()
