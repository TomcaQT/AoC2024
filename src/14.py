from copy import deepcopy
from sys import argv
from utils.utils import *
from aocd import get_data
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement
from operator import add
import re
from copy import deepcopy

class Robot:

    def __init__(self, pos, vel, bounds):
        self.pos: tuple = pos
        self.vel: tuple = vel
        self.bounds: tuple = bounds

    def move(self):
        new_x, new_y = map(add, self.pos, self.vel)
        x_l, y_l = self.bounds
        new_x, new_y = new_x % x_l, new_y % y_l
        self.pos = (new_x, new_y)
        return self.pos

    def __repr__(self):
        return f"Robot {self.pos=}, v={self.vel}"

def solve(data, test=False):
    if test:
        print(data[0])
    total = 0
    bounds = data[0].bounds

    for s in range(100):
        for r in data:
            r.move()


    q1, q2, q3, q4 = list(),list(),list(),list()
    x_l, y_l = bounds[0] // 2, bounds[1] // 2

    for r in data:
        x, y = r.pos
        if x < x_l and y < y_l:
            q1.append(r)
        elif x < x_l and y > y_l:
            q2.append(r)
        elif x > x_l and y < y_l:
            q3.append(r)
        elif x > x_l and y > y_l:
            q4.append(r)


    total = len(q1) * len(q2) * len(q3) * len(q4)

    print_c(total)

def pprint(grid):
    for y in grid:
        for x in y:
            print(x, end="")
        print("|")

def solve2(data, test=False):
    if test:
        print(data[0])
    total = 0
    bounds = data[0].bounds
    grid = [['.' for x in range(bounds[0])] for y in range(bounds[1])]
    pprint(grid)
    for s in range(10000):

        new_grid = deepcopy(grid)
        for r in data:
            x,y = r.move()
            new_grid[y][x] = "#"
        if s % 101 == 3:
            print(f"Seconds elapsed: {s+1}")
            pprint(new_grid)
            input()





def parse_data(indata = None):
    bounds = (101,103)
    if not indata:
        indata = open('data/14.in', 'r')
        bounds = (11,7)
    data = []
    for l in indata:
        m = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", l.strip())
        r = Robot(
            pos=(int(m[1]), int(m[2])),
            vel=(int(m[3]), int(m[4])),
            bounds=bounds)
        data.append(r)
    return data


if __name__ == '__main__':
    data = parse_data()
    data_real = parse_data(get_data(day=14, year=2024).splitlines(True))
    if len(argv) < 2 or argv[1] != '2':
        print("Part1 test:")
        solve(data, test=True)
        print("Part1: ")
        solve(data_real)
    else:
        #solve2(data, test=True)
        print("Part2: ")
        solve2(data_real)