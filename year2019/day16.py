def compute_pattern(index) -> list:
    pattern = [0, 1, 0, -1]
    output_pattern = []
    for i in pattern:
        output_pattern += index*[i]
    output_pattern.pop(0)
    return output_pattern

def compute_signal():
    with open("day16.txt", 'r') as fp:
        signal = [int(x) for x in fp.read().rstrip('\n')]

    new_signal = []

    return

# print(compute_pattern(1))

compute_signal()
