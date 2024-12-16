from collections import Counter, defaultdict
from itertools import combinations
from aocd import get_data

def solve(data, test=False):
    if test:
        print(data)
    y_l, x_l = len(data), len(data[0])

    antenas = defaultdict(list)
    signals = set()

    for y in range(y_l):
        for x in range(x_l):
            if data[y][x] != ".":
                antenas[data[y][x]].append((x,y))

    for a, pos in antenas.items():
        #print(f"{a}:: {pos}")
        for c in combinations(pos,2):
            #print(c)
            x1, y1 = c[0]
            x2, y2 = c[1]
            dx, dy = x1 - x2, y1 - y2
            new_x, new_y = x1+dx, y1+dy
            new_x2, new_y2 = x2-dx, y2-dy
            #print(f"{dx=},{dy=}")
            #print(f"n1:{new_x}:{new_y}")
            #print(f"n2:{new_x2}:{new_y2}")
            if new_x >= 0 and new_x < x_l and new_y >= 0 and new_y < y_l:
                signals.add((new_x,new_y))
            if new_x2 >= 0 and new_x2 < x_l and new_y2 >= 0 and new_y2 < y_l:
                signals.add((new_x2,new_y2))
    print(len(signals))
    # print(signals)
    #
    # for y in range(y_l):
    #     for x in range(x_l):
    #         if (x,y) in signals:
    #             print("#", end='')
    #         else:
    #             print(data[y][x], end='')
    #     print()



def solve2(data, test=False):
    y_l, x_l = len(data), len(data[0])

    antenas = defaultdict(list)
    signals = set()

    for y in range(y_l):
        for x in range(x_l):
            if data[y][x] != ".":
                antenas[data[y][x]].append((x,y))

    for a, pos in antenas.items():
        #print(f"{a}:: {pos}")
        for c in combinations(pos,2):
            #print(f"2{c}")
            x1, y1 = c[0]
            x2, y2 = c[1]
            signals.add((x1,y1))
            signals.add((x2,y2))
            dx, dy = x1 - x2, y1 - y2
            new_x, new_y = x1+dx, y1+dy
            while new_x >= 0 and new_x < x_l and new_y >= 0 and new_y < y_l:
                signals.add((new_x,new_y))
                new_x, new_y = new_x+dx, new_y+dy

            new_x2, new_y2 = x2-dx, y2-dy
            while new_x2 >= 0 and new_x2 < x_l and new_y2 >= 0 and new_y2 < y_l:
                signals.add((new_x2,new_y2))
                new_x2, new_y2 = new_x2-dx, new_y2-dy
            #print(f"{dx=},{dy=}")
            #print(f"n1:{new_x}:{new_y}")
            #print(f"n2:{new_x2}:{new_y2}")

    print(len(signals))
    # print(signals)
    #
    # for y in range(y_l):
    #     for x in range(x_l):
    #         if (x,y) in signals:
    #             print("#", end='')
    #         else:
    #             print(data[y][x], end='')
    #     print()


def read_file():
    data = []
    with open('../data/8.in', 'r') as f:
        return [list(l.strip())for l in f.readlines()]


if __name__ == '__main__':
    data = read_file()
    print("Testing data: ")
    solve(data, test=True)
    solve2(data, test=True)
