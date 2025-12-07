from sys import argv
from utils.utils import *
from aocd import get_data, submit
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement


DAY, YEAR = 1, 2025

def solve(data, test=False, autosubmit=False):
    if test:
        print(data)
        autosubmit = False
    total = 0
    pos = 50
    for line in data:
        step = int(line[1:])
        dir = -1 if line[0] == 'L' else 1

        pos += (step * dir)
        pos %= 100
        if pos == 0:
            total += 1
        #print(pos)


    print_c(total)
    if autosubmit:
        submit(total,part="a", day=DAY, year=YEAR)


def solve2(data, test=False, autosubmit=False):
    if test:
        print(data)
        autosubmit = False
    total = 0
    pos = 50
    prev_pos = -1
    for line in data:
        step = int(line[1:])
        dir = -1 if line[0] == 'L' else 1
        print(f"Befor step:{step} pos:{pos}, total:{total}")
        total += step // 100
        step %= 100
        prev_pos = pos
        pos += step * dir
        #print(pos)
        if step == 0:
            continue
        if pos == 0 or pos == 100:
          pos = 0
          total += 1
        elif pos > 100:
            total += 1
            pos = pos - 100
        elif pos < 0:
            if prev_pos != 0:
                total += 1
            pos = 100 + pos
        print(f"After step:{step} pos:{pos}, total:{total}")
        print("====")

    print_c(total)
    if autosubmit:
        submit(total,part="a", day=DAY, year=YEAR)


def parse_data(indata = None):
    if not indata:
        indata = open('data/1.in', 'r')
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