from sys import argv
from utils.utils import *
from aocd import get_data
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement

def get(x,y, data):
    y_l, x_l = len(data), len(data[0])
    if x<0 or x>=x_l or y<0 or y>=y_l: return -1
    return data[y][x]

def bfs(data, start):
    q = [start]
    seen = set()
    seen.add(start)
    y_l, x_l = len(data), len(data[0])
    peri = 0
    sides = 0

    while len(q) > 0:
        curr = q.pop(0)
        x,y = curr
        peri += 4
        for dx,dy in ((-1,-1),(-1,1),(1,-1),(1,1)):
            a,b,c,d=get(x,y,data),get(x+dx,y,data),get(x,y+dy,data),get(x+dx,y+dy,data)
            if (a!=b and a!=c) or (a==b and a==c and a!=d):
                sides +=1
        for d in [(1,0), (-1,0), (0,1), (0,-1)]:
            xn, yn = x+d[0], y+d[1]
            if xn >= 0 and xn < x_l and yn >= 0 and yn < y_l:
                # in bounds
                if data[yn][xn] == data[y][x]:
                    peri -= 1
                    if (xn,yn) not in seen:
                        seen.add((xn,yn))
                        q.append((xn,yn))

    return peri, seen, sides


def solve(data, test=False):
    if test:
        print(data)
    total = 0
    y_l, x_l = len(data), len(data[0])
    seen = set()
    for y in range(y_l):
        for x in range(x_l):
            if (x,y) not in seen:
                peri, s, _ = bfs(data, (x,y))
                seen.update(s)
                total += peri * len(s)

    print_c(total)


def solve2(data, test=False):
    if test:
        print(data)
    total = 0
    if test:
        print(data)
    total = 0
    y_l, x_l = len(data), len(data[0])
    seen = set()
    for y in range(y_l):
        for x in range(x_l):
            if (x,y) not in seen:
                peri, s, sides = bfs(data, (x,y))
                seen.update(s)
                total += len(s) * sides
    print_c(total)


def parse_data(indata = None):
    if not indata:
        indata = open('data/12.in', 'r')
    return [l.strip() for l in indata]


if __name__ == '__main__':
    data = parse_data()
    data_real = parse_data(get_data(day=12, year=2024).splitlines(True))
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