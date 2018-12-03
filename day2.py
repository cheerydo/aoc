def count_letters(word, count):
    for letter in word:
        if word.count(letter) == count:
            return 1


def three_letters(word):
    for letter in word:
        if word.count(letter) == 3:
            return 1


with open("day2.txt") as f:
    input = f.read().splitlines()

    twos = 0
    threes = 0

    for word in input:
        if count_letters(word, 3):
            threes += 1
        if count_letters(word, 2):
            twos += 1

    checksum = threes * twos

    print(checksum)
