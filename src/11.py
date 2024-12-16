from sys import argv
from utils.utils import *
from aocd import get_data
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement
from tqdm import tqdm
from functools import lru_cache

def solve(data, test=False):
    if test:
        print(data)
    total = 0
    #y_l, x_l = len(data), len(data[0])
    stones = data[:]
    for _ in range(25):
        new_stones = []
        for s in stones:
            if s == 0:
                new_stones.append(1)
                continue
            ss = str(s)
            if len(ss) % 2 == 0:
                h = len(ss)//2
                new_stones.append(int(ss[0:h]))
                new_stones.append(int(ss[h:]))
                continue
            new_stones.append(s*2024)
        stones = new_stones

    total = len(stones)


    print_c(total)

@lru_cache()
def calculate(s):
    if s == 0:
       return [1]
    ss = str(s)
    if len(ss) % 2 == 0:
        h = len(ss)//2
        return [int(ss[0:h]),int(ss[h:])]
    return [s*2024]

def solve2(data, test=False):
    if test:
        print(data)
    total = 0
    #y_l, x_l = len(data), len(data[0])
    stones = Counter(data)
    for i in tqdm(range(75)):
        new_stones = Counter()
        for s, c in stones.items():
            new_stone = calculate(s)
            for ns in new_stone:
                new_stones[ns] += c
        stones = new_stones

    total = stones.total()


    print_c(total)


def parse_data(indata = None):
    if not indata:
        indata = open('data/11.in', 'r')
    d = [l.strip().split() for l in indata][0]
    return list(map(int, d))


if __name__ == '__main__':
    data = parse_data()
    data_real = parse_data(get_data(day=11, year=2024).splitlines(True))
    if len(argv) < 2 or argv[1] != '2':
        print("Part1 test:")
        solve(data, test=True)
        print("Part1: ")
        solve(data_real)
    else:
        #print("Part2 test:")
        #solve2(data, test=True)
        print("Part2: ")
        solve2(data_real)