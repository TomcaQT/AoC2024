from collections import Counter
from aocd import get_data

def solve(data):
    x,y = data
    x = sorted(x)
    y = sorted(y)
    diff = 0
    for i in range(len(x)):
        diff += abs(x[i] - y[i])
    print(diff)

def solve2(data):
    x = data[0]
    y = Counter(data[1])
    score = 0
    for xx in x:
        score += xx * y[xx]
    print(score)


def read_file():
    x,y = [], []
    with open('../data/1.in', 'r') as f:
        return [tuple(l.strip().split(' '))for l in lines]


if __name__ == '__main__':
    d = get_data(day=1, year=2024)
    print(d)
    data = read_file()
    solve(data)
    solve2(data)