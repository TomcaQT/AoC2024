from sys import argv
from utils.utils import *
from aocd import get_data, submit
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement
from tqdm import tqdm

DAY, YEAR = 3, 2025

def solve(data, test=False, autosubmit=False):
    if test:
        print(data)
        autosubmit = False
    total = 0

    for bank in data:
        print(bank)
        m, m2 = -1, -1
        for jolt in bank[:-1]:
            jolt = int(jolt)
            if jolt > m:
                m = jolt
                m2 = -1
            else:
                if jolt > m2:
                    m2 = jolt
        mm1 = m * 10 + m2
        mm2 = m * 10 + int(bank[-1])
        mm = max(mm1, mm2)
        print(mm)
        total += mm

    print_c(total)
    if autosubmit:
        submit(total,part="a", day=DAY, year=YEAR)


def solve2(data, test=False, autosubmit=False):
    if test:
        print(data)
        autosubmit = False
    total = 0


    for bank in tqdm(data):
        window_end = len(bank) - 11
        window_start = 0
        final = []
        while len(final) != 12:
            window = bank[window_start:window_end]
            m = max(window, key=int)
            final.append(int(m))
            w_index = window.index(m)
            window_end += 1
            window_start = window_start + w_index + 1

        final = "".join([str(x) for x in final])
        total += int(final)


    print_c(total)
    if autosubmit:
        submit(total,part="b", day=DAY, year=YEAR)


def parse_data(indata = None):
    if not indata:
        indata = open('data/3.in', 'r')
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