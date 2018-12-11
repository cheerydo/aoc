import re


def sort_dates(input):
    times = []

    for line in input:
        ts = re.search(r'\d+-\d+ \d+:\d+', line)
        if ts:
            times.append(ts.group())

    keys = sorted(times)

    s = [line for k in keys for line in input if k in line]

    return s


def find_guard(sorted_input):
    gr = re.compile(r'Guard #(\d+)')
    hm = re.compile(r'\d+:(\d+)')

    # First build a list of guards
    guards = {}
    for line in sorted_input:
        g = gr.search(line)
        if g:
            guards[g.group(1)] = []

    # Seed initial guard ID
    guard = gr.search(sorted_input[0]).group(1)

    # Pop through the list and find sleeps/wakes
    # and then append to guards dict
    while True:
        if len(sorted_input) < 1:
            break

        l = sorted_input.pop(0)
        minute = hm.search(l).group(1)
        if "asleep" in l:
            sleep = int(minute)
        elif "wakes" in l:
            woke = int(minute)
            # Let's just list all the minutes in the sleeping period and append to sleep times
            for x in range(woke - sleep):
                guards[guard].append(sleep + x)
        elif "Guard" in l:
            guard = gr.search(l).group(1)

    # Find guard with most sleeps by len
    sleepiest_guard = max(guards, key=lambda l: len(guards[l]))
    sleepiest_minute = max(guards[sleepiest_guard], key=lambda s: guards[sleepiest_guard].count(s))

    part_a = int(sleepiest_guard) * int(sleepiest_minute)

    #### PART TWO ####
    # Build a list of minutes to find how many guards slept on that minute
    minutes = {i: [] for i in range(60)}
    for guard in guards:
        l = guards[guard]
        for i in l:
            minutes[i].append(guard)

    most_occurrences = [0, 0, 0]
    for minute in minutes:
        if len(minutes[minute]) < 1:
            break
        # Find the guard who slept the most times for the given minute
        sleepiest_guard = max(minutes[minute], key=lambda s: minutes[minute].count(s))
        sleepiest_guard_count = minutes[minute].count(sleepiest_guard)
        if sleepiest_guard_count > most_occurrences[1]:
            most_occurrences = [int(sleepiest_guard), sleepiest_guard_count, minute]

    part_b = most_occurrences[0] * most_occurrences[2]

    return part_a, part_b


with open("input/day4.txt") as f:
    input = f.read().splitlines()
    sorted_input = sort_dates(input)

    a, b = find_guard(sorted_input)

    print(f'Part a is {a}, part b is {b}')

