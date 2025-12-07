from sys import argv
from utils.utils import *
from aocd import get_data, submit
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement
from copy import deepcopy


DAY, YEAR = 4, 2025

def solve(data, test=False, autosubmit=False):
    if test:
        print(data)
        autosubmit = False
    total = 0
    y_l, x_l = len(data), len(data[0])
    for y in range(y_l):
        for x in range(x_l):
            val = data[y][x]
            if val != "@":
                continue
            adj = 0
            for dy, dx in [(-1,0),(1,0),(0,-1),(0,1), (-1,-1),(-1,1),(1,-1),(1,1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < y_l and 0 <= nx < x_l:
                    if data[ny][nx] == "@":
                        adj += 1
            if adj < 4:
                total += 1






    print_c(total)
    if autosubmit:
        submit(total,part="a", day=DAY, year=YEAR)


def solve2(data, test=False, autosubmit=False):
    if test:
        print(data)
        autosubmit = False
    total = 0
    y_l, x_l = len(data), len(data[0])

    changed = True
    while changed:

        new_data = []
        changed = False
        for y in range(y_l):
            new_data.append("")
            for x in range(x_l):
                val = data[y][x]
                if val != "@":
                    if val == "#":
                        val = "."
                    new_data[y] += val
                    continue
                adj = 0
                for dy, dx in [(-1,0),(1,0),(0,-1),(0,1), (-1,-1),(-1,1),(1,-1),(1,1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < y_l and 0 <= nx < x_l:
                        if data[ny][nx] == "@":
                            adj += 1
                if adj < 4:
                    total += 1
                    new_data[y] += "#"
                    changed = True
                else:
                    new_data[y] += val
        data = [x[:] for x in new_data]



    print_c(total)
    if autosubmit:
        submit(total,part="b", day=DAY, year=YEAR)


def parse_data(indata = None):
    if not indata:
        indata = open('data/4.in', 'r')
    return [l.strip() for l in indata]


if __name__ == '__main__':
    data = parse_data()
    data_real = parse_data(get_data(day=DAY, year=YEAR).splitlines(True))

    autosubmit = len(argv) >= 3 and argv[2] == 's'

    if len(argv) < 2 or argv[1] != '2':
        print("Part1 test:")
        solve(data, test=True)
        print("Part1: ")
        solve(data_real, autosubmit=autosubmit)
    else:
        print("Part2 test:")
        solve2(data, test=True)
        print("Part2: ")
        solve2(data_real, autosubmit=autosubmit)