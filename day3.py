import re

with open("input/day3.txt") as f:
    input = f.read().splitlines()

    # Only grab last two words in line and put into list
    inst_list = [list(inst.split(' ')) for inst in input]

    coords = set()
    dups = set()

    # Coords as keys in a dictionary which we'll append ids to
    fabric = {(x + 1, y + 1): [] for x in range(1000) for y in range(1000)}

    r = re.compile(r'[0-9]{1,4}')

    for inst in inst_list:
        idn = r.search(inst[0]).group()

        xycoords = r.findall(inst[2])
        x, y = [int(i) + 1 for i in xycoords]

        ranges = r.findall(inst[3])
        loop1, loop2 = [int(i) for i in ranges]

        # Loops through the instructions and generates coordinates, adding to dups if we've already seen it
        for r1 in range(loop1):
            y1 = y
            for r2 in range(loop2):
                if (x, y1) in coords:
                    dups.add((x, y1))
                coords.add((x, y1))

                # Append the ids as we loop
                fabric[(x, y1)].append(idn)
                y1 += 1
            x += 1

    # THIS SOME SHITTY CODE I DONE WROTE
    # But this first line grabs the list of ids in the fabric that have more than one element
    # since those are the ids of overlapping territory
    dupes = [fabric[t] for t in fabric if len(fabric[t]) > 1]

    # This next line flattens the list of overlapping ids and dedupes it with set()
    de_dupes = set([int(idn) for series in dupes for idn in series])

    # Finally we find the one value missing from our range (since only one id should have 0 overlap)
    missing = [x + 1 for x in range(1301) if x + 1 not in de_dupes]

    print(f'Overlapping fabric in inches: {len(dups)}')
    print(f"The only ID which doesn't overlap is {missing[0]}")
