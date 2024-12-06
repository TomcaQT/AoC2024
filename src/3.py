from collections import Counter
from aocd import get_data
import re

def solve(data, test=False):
    if test:
        print(data)
    total = 0

    matches = re.findall(r"mul\((\d+),(\d+)\)", data)
    for m in matches:
        a,b = m
        total += int(a) * int(b)
    print(total)


def solve2(data, test=False):

    if test:
        data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        print(data)
    total = 0
    enabled = True
    matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data)
    for m in matches:
        if m[2] == 'do()':
            enabled = True
        elif m[3] == "don't()":
            enabled = False
        else:
            if enabled:
                a,b = m[0], m[1]
                total += int(a) * int(b)
    print(total)



def read_file():
    data = []
    with open('../data/3.in', 'r') as f:
        return f.readlines()[0]


if __name__ == '__main__':
    data = read_file()
    print("Testing data: ")
    solve(data, test=False)
    solve2(data, test=False)
    data_real = get_data(day=3, year=2024)
    print("Real data: ")
    solve(data_real)
    solve2(data_real)