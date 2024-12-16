from sys import argv
from utils.utils import *
from aocd import get_data
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement

moves = {
    "^": (0,-1),
    "v": (0,1),
    "<": (-1,0),
    ">": (1,0)
}

def gprint(grid):
    for y in grid:
        for x in y:
            print(x, end="")
        print()

def solve(data, test=False):
    if test:
        print(data)
    total = 0
    grid, movements = data
    y_l, x_l = len(grid), len(grid[0])
    curr = (-1,-1)
    # find robot:
    for y in range(y_l):
        for x in range(x_l):
            if grid[y][x] == "@":
                curr = (x,y)

    for m in movements:
        x, y = curr
        mx, my = moves[m]
        nx, ny = x+mx, y+my
        if grid[ny][nx] == ".":
            # move
            grid[ny][nx] = "@"
            curr = (nx, ny)
            grid[y][x] = "."
        elif grid[ny][nx] == "O":
            bx, by = nx, ny
            movable = False
            while True:
                bx, by = bx+mx, by+my
                if grid[by][bx] == "#":
                    break
                elif grid[by][bx] == ".":
                    movable = True
                    grid[by][bx] = "O"
                    #grid[ny][nx] = "."
                    break
            if movable:
                grid[ny][nx] = "@"
                curr = (nx, ny)
                grid[y][x] = "."
        #gprint(grid)

    # count gps
    for y in range(y_l):
        for x in range(x_l):
            if grid[y][x] == "O":
                total += 100*y + x


    print_c(total)


def solve2(data, test=False):
    if test:
        print(data)
    total = 0
    grid, movements = data
    y_l, x_l = len(grid), len(grid[0])
    curr = (-1,-1)
    # find robot:
    for y in range(y_l):
        for x in range(x_l):
            if grid[y][x] == "@":
                curr = (x,y)

    for m in movements:
        x, y = curr
        mx, my = moves[m]
        nx, ny = x+mx, y+my
        if grid[ny][nx] == ".":
            # move
            grid[ny][nx] = "@"
            curr = (nx, ny)
            grid[y][x] = "."
        elif grid[ny][nx] == "O":
            bx, by = nx, ny
            movable = False
            while True:
                bx, by = bx+mx, by+my
                if grid[by][bx] == "#":
                    break
                elif grid[by][bx] == ".":
                    movable = True
                    grid[by][bx] = "O"
                    #grid[ny][nx] = "."
                    break
            if movable:
                grid[ny][nx] = "@"
                curr = (nx, ny)
                grid[y][x] = "."
        #gprint(grid)

    # count gps
    for y in range(y_l):
        for x in range(x_l):
            if grid[y][x] == "O":
                total += 100*y + x



    print_c(total)


def parse_data(indata = None):
    if not indata:
        indata = open('data/15.in', 'r')
    grid, movements, g = [], "", True
    for l in indata:
        if l == "\n":
            g = False
            continue
        if g:
            grid.append(list(l.strip()))
        else:
            movements += l.strip()

    return (grid, movements)


if __name__ == '__main__':
    data = parse_data()
    data_real = parse_data(get_data(day=15, year=2024).splitlines(True))
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