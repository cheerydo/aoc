def find_duplicate_freq(nums):
    freq_list = set([0])
    freq = 0
    dup_freq = None

    while not dup_freq:
    # Build list of frequencies seen
        for i in nums:
            new_freq = freq + i
            if new_freq in freq_list:
                dup_freq = new_freq
                break
            else:
                freq = new_freq
                freq_list.add(new_freq)

    return dup_freq

with open("aoc1.txt") as f:
    input = [int(x) for x in f.read().splitlines()]

    final_freq = sum(input)
    dup_freq = find_duplicate_freq(input)

    print(final_freq)
    print(dup_freq)
