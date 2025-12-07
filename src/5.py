from sys import argv
from utils.utils import *
from aocd import get_data, submit
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement
from tqdm import tqdm

DAY, YEAR = 5, 2025

def solve(data, test=False, autosubmit=False):
    if test:
        print(data)
        autosubmit = False
    total = 0
    ranges, ids = [], []
    loading_ids = False
    for line in data:
        if line == "":
            loading_ids = True
            continue
        if not loading_ids:
            x,y = line.split("-")
            ranges.append( (int(x), int(y)) )
        else:
            ids.append(int(line))
    for id in ids:
        for x,y in ranges:
            if x <= id <= y:
                total += 1
                break



    print_c(total)
    if autosubmit:
        submit(total,part="a", day=DAY, year=YEAR)


def merge(range1, range2):
    x1,y1 = range1
    x2,y2 = range2
    # check if they overlap
    if x1 <= x2 <= y1 or x2 <= x1 <= y2:
        return (min(x1,x2), max(y1,y2))
    return None


def solve2(data, test=False, autosubmit=False):
    if test:
        print(data)
        autosubmit = False
    total = 0
    ranges = []
    fresh = set()
    for line in data:
        if line == "":
            break
        x,y = line.split("-")
        # try to merge
        new_range = (int(x), int(y))
        new_ranges = []
        for r in ranges:
            merged = merge(r, new_range)
            if merged:
                new_range = merged
            else:
                new_ranges.append(r)
        new_ranges.append(new_range)
        ranges = new_ranges[:]

    for r in ranges:
        x,y = r
        total += (y - x + 1)

    print_c(total)
    if autosubmit:
        submit(total,part="b", day=DAY, year=YEAR)


def parse_data(indata = None):
    if not indata:
        indata = open('data/5.in', 'r')
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