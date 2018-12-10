import re
from datetime import datetime

with open("day4.txt") as f:
    input = f.read().splitlines()

    guards = {}

    # Build a list of guards
    for t in input:
        g = re.search(r'Guard \#([0-9]+)', t)
        if g:
            guards[g.group(1)] = {}

    # Sort dates
    

print(guards)
