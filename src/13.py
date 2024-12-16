import math
from sys import argv
from utils.utils import *
from aocd import get_data
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement
import re


def rec(data, part2=False):
    # x* A_x + y* B_x = C_x
    A_x, A_y, B_x, B_y, C_x, C_y = data
    if part2:
        C_x, C_y = C_x + 10000000000000, C_y + 10000000000000
    a = (B_y * C_x - B_x * C_y) / (B_y * A_x - B_x * A_y)
    b = (C_x - A_x * a) / B_x
    if a == int(a) and b == int(b):
        return int(a*3 + b)
    return None





def solve(data, test=False):
    if test:
        print(data)
    total = 0
    for machine in data:
        cost = rec(machine)
        if cost:
            total += cost

    total = 0
    for machine in data:
        cost = 0
        if total:
            total += cost

    print_c(total)


def solve2(data, test=False):
    if test:
        print(data)
    total = 0
    for machine in data:
        cost = rec(machine, True)
        if cost:
            total += cost


    print_c(total)


def parse_data(indata = None):
    if not indata:
        indata = open('data/13.in', 'r')
    machine = tuple()
    data = []
    for l in indata:
        if l == '\n':
            data.append(machine)
            machine = tuple()
        elif m := re.findall(r"X\+(\d+), Y\+(\d+)", l):
            machine = machine + tuple(map(int,m[0]))
        elif m := re.findall(r"X=(\d+), Y=(\d+)", l):
            machine = machine + tuple(map(int,m[0]))
    data.append(machine)
    return data


if __name__ == '__main__':
    data = parse_data()
    data_real = parse_data(get_data(day=13, year=2024).splitlines(True))
    if len(argv) < 2 or argv[1] != '2':
        print("Part1 test:")
        solve(data, test=True)
        print("Part1: ")
        solve(data_real)
    else:
        print("Part2 test:")
        solve2(data, test=True)
        print("Part2: ")
        solve2(data_real)