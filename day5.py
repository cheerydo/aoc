def compare(pair):
    if pair[0] == pair[1].upper() or pair[0] == pair[1].lower():
        return True


def loop(input):
    for index in range(1, len(input)):
        if compare((input[index - 1], input[index])):
            del input[index]
            del input[index - 1]
            return input


with open("input/day5.txt") as f:
    input = list(f.read())
    output = []

    while True:
        output = input
        input = loop(input)
        if not input:
            break

    print(len(output))

