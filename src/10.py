from sys import argv
from utils.utils import *
from aocd import get_data
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement

def get_neis(data, c):
    neis = []
    x,y = c
    y_l, x_l = len(data), len(data[0])
    for d in [(1,0),(-1,0),(0,1),(0,-1)]:
        new_y, new_x = y+d[1],x+d[0]
        if new_x >= 0 and new_x < x_l and new_y >= 0 and new_y < y_l:
            if data[y][x] +1 == data[new_y][new_x]:
                neis.append((new_x,new_y))
    return neis


def dfs(data, curr):
    q = [curr]
    total = set()
    while len(q) > 0:
        c = q.pop(0)
        x,y = c
        if data[y][x] == 9:
            total.add(c)
        for n in get_neis(data,c):
            q.append(n)
    return len(total)

def bfs(data, curr):
    q = [curr]
    total = 0
    while len(q) > 0:
        c = q.pop(0)
        x,y = c
        if data[y][x] == 9:
            total += 1
        for n in get_neis(data,c):
            q.append(n)
    return total


def solve(data, test=False):
    if test:
        print(data)
    total = 0
    y_l, x_l = len(data), len(data[0])
    for y in range(y_l):
        for x in range(x_l):
            if data[y][x] == 0:
                t = dfs(data, (x,y))
                total += t

    print_c(total)



def solve2(data, test=False):
    if test:
        print(data)
    total = 0
    y_l, x_l = len(data), len(data[0])
    for y in range(y_l):
        for x in range(x_l):
            if data[y][x] == 0:
                t = bfs(data, (x,y))
                total += t

    print_c(total)


def parse_data(indata = None):
    if not indata:
        indata = open('data/10.in', 'r')
    return [[int(x) for x in l.strip()] for l in indata ]


if __name__ == '__main__':
    data = parse_data()
    data_real = parse_data(get_data(day=10, year=2024).splitlines(True))
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