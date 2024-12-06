from collections import Counter
from aocd import get_data
from copy import deepcopy

def solve(data, test=False):
    dirs = [(0,-1), (1,0), (0,1), (-1, 0)]
    total = set()
    x,y, d, dir = 0,0, 0, dirs[0]
    x_l, y_l = len(data[0]), len(data)
    # find player
    for xx in range(x_l):
        for yy in range(y_l):
            if data[yy][xx] == "^":
                x = xx
                y = yy


    while True:
        x_d, y_d = dir
        if (y+y_d<0 or y+y_d >= y_l) or (x+x_d < 0 or x+x_d >= x_l):
            break
        if data[y+y_d][x+x_d] == "#":
            #turn
            d+=1
            if d >= len(dirs):
                d = 0
            dir = dirs[d]
        else:
            total.add((x,y))
            x = x+x_d
            y = y+y_d
    print(len(total) + 1 )


def check_loop(data, x, y):
    dirs = [(0,-1), (1,0), (0,1), (-1, 0)]
    total = set()
    d, dir = 0, dirs[0]
    x_l, y_l = len(data[0]), len(data)
    while True:
        x_d, y_d = dir
        if (x,y,x_d, y_d) in total:
            return True
        if (y+y_d<0 or y+y_d >= y_l) or (x+x_d < 0 or x+x_d >= x_l):
            return False
        if data[y+y_d][x+x_d] == "#":
            #turn
            d+=1
            if d >= len(dirs):
                d = 0
            dir = dirs[d]
            total.add((x,y,x_d, y_d))
        else:
            total.add((x,y,x_d, y_d))
            x = x+x_d
            y = y+y_d

def solve2(data, test=False):
    x,y = 0,0
    x_l, y_l = len(data[0]), len(data)
    t = 0
    # find player
    for xx in range(x_l):
        for yy in range(y_l):
            if data[yy][xx] == "^":
                x = xx
                y = yy

    for xx in range(x_l):
        for yy in range(y_l):
            if data[yy][xx] == ".":
                new_data = deepcopy(data)
                new_data[yy][xx] = "#"
                if check_loop(new_data,x,y):
                    t += 1
    print(t)



def read_file():
    data = []
    with open('../data/6.in', 'r') as f:
        return [list(l.strip())for l in f.readlines()]



if __name__ == '__main__':
    data = read_file()
    print("Testing data: ")
    solve(data, test=True)
    solve2(data, test=True)