from sys import argv
from utils.utils import *
from aocd import get_data, submit
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement


DAY, YEAR = 7, 2025

def solve(data, test=False, autosubmit=False):
    if test:
        print(data)
        autosubmit = False
    total = 0
    y_l, x_l = len(data), len(data[0])
    for y in range(y_l):
        if y == y_l - 1:
            break
        for x in range(x_l):
            val = data[y][x]
            if val == "." or val == "^":
                continue
            if data[y+1][x] != "^":
                data[y+1][x] = "S"
                continue
            x1, x2 = x-1, x+1
            if x1 >= 0:
                data[y+1][x1] = "S"
            if x2 < x_l:
                data[y+1][x2] = "S"
            total += 1

    print_c(total)
    if autosubmit:
        submit(total,part="a", day=DAY, year=YEAR)
    return data


def solve2(data, test=False, autosubmit=False):
    if test:
        print(data)
        autosubmit = False
    total = 0
    y_l, x_l = len(data), len(data[0])
    quants  = [1 if val == "S"  else 0 for val in data[-1]]
    for y in range(y_l-1,0, -1):
        new_quants = [0 for _ in quants]
        for x in range(x_l):
            val = data[y][x]
            if val == ".":
                continue
            if val == "S" and data[y-1][x] == "S":
                new_quants[x] += quants[x]
            if val == "^":
                to_add = quants[x-1] + quants[x+1]
                new_quants[x] += to_add



        quants = new_quants[:]

    total = sum(quants)

    print_c(total)
    if autosubmit:
        submit(total,part="b", day=DAY, year=YEAR)


def parse_data(indata = None):
    if not indata:
        indata = open('data/7.in', 'r')
    return [list(l.strip()) for l in indata]


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
        solve2(solve(data), test=True)
        print("Part2: ")
        solve2(solve(data_real), autosubmit=autosubmit)