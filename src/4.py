from collections import Counter
from aocd import get_data

def solve(data, test=False):
    total = 0
    if test:
        print(data)
    t, t_r = "XMAS", "SAMX"
    x_l, y_l = len(data[0]), len(data),
    #
    for x in data:
        for y in range(0, x_l-3):
            if x[y:y+4] == t or x[y:y+4] == t_r:
                total += 1

    for y in range(0, y_l-3):
        for x in range(0, x_l):
            w = data[y][x] + data[y+1][x] + data[y+2][x] + data[y+3][x]
            if w == t or w[::-1] == t:
                total += 1

    for y in range(0, y_l-3):
        for x in range(0, x_l-3):
            w = data[y][x] + data[y+1][x+1] + data[y+2][x+2] + data[y+3][x+3]
            if w == t or w[::-1] == t:
                total += 1

    for y in range(3, y_l):
        for x in range(0, x_l-3):
            w = data[y][x] + data[y-1][x+1] + data[y-2][x+2] + data[y-3][x+3]
            if w == t or w[::-1] == t:
                total += 1



    print(total)


def solve2(data, test=False):
    total = 0
    if test:
        print(data)
    t, t_r = "MAS", "SAM"
    x_l, y_l = len(data[0]), len(data),


    for y in range(1, y_l-1):
        for x in range(1, x_l-1):
            w1 = data[y-1][x-1] + data[y][x] + data[y+1][x+1]
            w2 = data[y-1][x+1] + data[y][x] + data[y+1][x-1]
            if (w1 == t or w1 == t_r) and (w2 == t or w2 == t_r):
                total += 1

    print(total)


def read_file():
    data = []
    with open('../data/4.in', 'r') as f:
        return [l.strip() for l in f]


if __name__ == '__main__':
    data = read_file()
    print("Testing data: ")
    solve(data, test=True)
    solve2(data, test=False)
    data_real = get_data(day=4, year=2024)
    print("Real data: ")
    solve(data_real)
    solve2(data_real)