def find_duplicate_freq(nums):
    freq_list = set([0])
    freq = 0
    dup_freq = None

    while not dup_freq:
        for i in nums:
            new_freq = freq + i
            if new_freq in freq_list:
                return new_freq
            else:
                freq = new_freq
                freq_list.add(new_freq)


with open("day1.txt") as f:
    input = [int(x) for x in f.read().splitlines()]

    final_freq = sum(input)
    dup_freq = find_duplicate_freq(input)

    print(final_freq)
    print(dup_freq)
