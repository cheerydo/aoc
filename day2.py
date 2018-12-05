def count_letters(word, count):
    for letter in word:
        if word.count(letter) == count:
            return 1


def find_common_strings(words):
    zipped = []
    common_strings = []

    # Loops over the list and returns index
    # of all combinations, then zips each combo
    # for comparison
    for i, item in enumerate(words):
        for r in range(len(words) - i):
            if i != i + r:
                a = zip(item, words[i + r])
                zipped.append(list(a))

    # Now we have a list of tuples, we'll compare
    # each string and add 1 to a diff count, if
    # diff == 1 then we have our strings
    for item in zipped:
        diff = 0
        for letter in item:
            if letter[0] == letter[1]:
                diff += 1
        if diff == 1:
            common_strings = item

    # Now we return common letters and unzip
    final_strings = list(zip(*[t for t in common_strings if t[0] == t[1]]))

    return ''.join(final_strings[0])


with open("input/day2.txt") as f:
    input = f.read().splitlines()

    twos = 0
    threes = 0

    for word in input:
        if count_letters(word, 2):
            twos += 1
        if count_letters(word, 3):
            threes += 1

    checksum = threes * twos
    final_string = find_common_strings(input)

    print(final_string)
