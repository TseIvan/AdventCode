from collections import OrderedDict

def day8(f1:str="day8.txt") -> None:
    # 25 by 6
    with open(f1, 'r') as fp:
        text_from_file = list(fp.read().rstrip('\n'))

    layer = 25*6
    dictionary = OrderedDict()
    for i in range(0,len(text_from_file),layer):
        partition = text_from_file[i:i+layer]
        dictionary["".join(partition)] = partition.count('0')

    lowest = min(dictionary,key=dictionary.get)
    print(int(lowest.count('1'))*int(lowest.count('2')),flush = True)

    # pixel: 0 is black, 1 is white, and 2 is transparent.
    # The layers are rendered with the first layer in front and the last layer in back.
    output = [2]*layer # initialize all to transparent
    for i in range(0,layer):
        for k,v in dictionary.items():
            pixel = int(list(k)[i]) # layer by priority, by color
            if pixel < 2:
                output[i] = pixel
                break
    # 25 wide
    for i in range(0,len(output),25):
        print(output[i:i+25])
    #KFABY
    return


if __name__ == "__main__":
    day8()
