from sys import argv
from utils.utils import *
from aocd import get_data
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement
from copy import deepcopy
from queue import PriorityQueue



def solve(data, test=False):
    if test:
        print(data)
    total = float("inf")
    start, end = (-1,-1), (-1,-1)
    y_l, x_l = len(data), len(data[0])
    for y in range(y_l):
        for x in range(x_l):
            if data[y][x] == "S":
                start = (x,y)
            if data[y][x] == "E":
                end = (x,y)

    d = {}
    q = PriorityQueue()
    q.put((0,(start, (1,0))))

    while not q.empty():
        s, xx = q.get()
        curr, dir = xx
        x,y = curr
        if data[y][x] == "#":
            continue
        if data[y][x] == "E":
            total = min(total, s)
        # straight
        xd, yd = dir

        if not(tmp := d.get(((x+xd,y+yd), (xd,yd))))  or tmp > s+1:
            q.put((s+1,((x+xd,y+yd) , (xd, yd))) )
            d[((x+xd,y+yd), (xd,yd))] = s+1

        xd, yd = yd, xd
        if not(tmp := d.get(((x+xd,y+yd), (xd,yd)))) or tmp > s+1001:
            q.put((s+1001,((x+xd,y+yd) , (xd, yd))) )
            d[((x+xd,y+yd), (xd,yd))] = s+1001

        xd, yd = -xd, -yd
        if not(tmp := d.get(((x+xd,y+yd), (xd,yd)))) or tmp > s+1001:
            q.put((s+1001,((x+xd,y+yd) , (xd, yd))))
            d[((x+xd,y+yd), (xd,yd))] = s+1001



    print_c(total)


def solve2(data, test=False):
    if test:
        print(data)
    total, min_path = float("inf"), set()
    start, end = (-1,-1), (-1,-1)
    y_l, x_l = len(data), len(data[0])
    for y in range(y_l):
        for x in range(x_l):
            if data[y][x] == "S":
                start = (x,y)
            if data[y][x] == "E":
                end = (x,y)

    d = {}
    q = PriorityQueue()
    q.put((0,(start, (1,0), list())))

    while not q.empty():
        s, xx = q.get()
        curr, dir, path = xx
        x,y = curr
        new_path = path[:]
        new_path.append(curr)
        if data[y][x] == "#":
            continue
        if data[y][x] == "E":
            if total > s:
                total = s
                min_path = set(new_path)
            elif total == s:
                min_path.update(new_path)
        # straight
        xd, yd = dir

        if not(tmp := d.get(((x+xd,y+yd), (xd,yd))))  or tmp >= s+1:
            q.put((s+1,((x+xd,y+yd) , (xd, yd), new_path)) )
            d[((x+xd,y+yd), (xd,yd))] = s+1

        xd, yd = yd, xd
        if not(tmp := d.get(((x+xd,y+yd), (xd,yd)))) or tmp >= s+1001:
            q.put((s+1001,((x+xd,y+yd) , (xd, yd), new_path)) )
            d[((x+xd,y+yd), (xd,yd))] = s+1001

        xd, yd = -xd, -yd
        if not(tmp := d.get(((x+xd,y+yd), (xd,yd)))) or tmp >= s+1001:
            q.put((s+1001,((x+xd,y+yd) , (xd, yd), new_path)) )
            d[((x+xd,y+yd), (xd,yd))] = s+1001




    print_c(len(min_path))


def parse_data(indata = None):
    if not indata:
        indata = open('data/16.in', 'r')
    return [l.strip() for l in indata]


if __name__ == '__main__':
    data = parse_data()
    data_real = parse_data(get_data(day=16, year=2024).splitlines(True))
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