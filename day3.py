import re

with open("day3.txt") as f:
    input = f.read().splitlines()

    # Only grab last two words in line and put into list
    inst_list = [list(inst.split(' ')) for inst in input]

    coords = set()
    dups = set()

    r = re.compile(r'[0-9]{1,3}')

    for inst in inst_list:
        xycoords = r.findall(inst[2])
        x, y = [int(i) for i in xycoords]

        ranges = r.findall(inst[3])
        loop1, loop2 = [int(i) for i in ranges]

        for r1 in range(loop1):
            y1 = y
            for r2 in range(loop2):
                if (x, y1) in coords:
                    dups.add((x, y1))
                coords.add((x, y1))
                y1 += 1
            x += 1

    print(len(dups))
