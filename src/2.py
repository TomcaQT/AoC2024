from sys import argv
from utils.utils import *
from aocd import get_data, submit
from collections import Counter, defaultdict
from itertools import combinations, permutations, product, combinations_with_replacement
from functools import lru_cache

DAY, YEAR = 2, 2025

@lru_cache(maxsize=None)
def is_valid(id: str | int) -> bool:
    id = str(id)
    if len(id) % 2 != 0:
        return True
    id_lenh = int(len(id) / 2)
    #print(id_lenh)
    if id[:id_lenh] == id[id_lenh:]:
        return False
    return True


def solve(data, test=False, autosubmit=False):
    if test:
        print(data)
        autosubmit = False
    total = 0
    for interval in data:
        x,y = interval.split("-")
        for i in range(int(x), int(y)+1):
            if not is_valid(i):
                total += i


    print_c(total)
    if autosubmit:
        submit(total,part="a", day=DAY, year=YEAR)

def check_repeat(id, seq):
    seq_len = len(seq)
    for i in range(0, len(id), seq_len):
        if id == "111":
            print(f" {seq} vs {id[i:i+seq_len]}")
        if seq != id[i:i+seq_len]:
            return False
    return True

@lru_cache(maxsize=None)
def is_valid2(id: str | int) -> bool:
    id = str(id)
    id_lenh, id_len = int(len(id) / 2), len(id)
    for i in range(1,id_lenh+1):
        if id == "111":
            print(i)
        if id_len % i != 0:
            continue
        seq = id[:i]
        if check_repeat(id, seq):
            return False
    return True



def solve2(data, test=False, autosubmit=False):
    if test:
        print(data)
        autosubmit = False
    total = 0
    for interval in data:
        x,y = interval.split("-")
        for i in range(int(x), int(y)+1):
            if not is_valid2(i):
                if test:
                    print(f"{i} not valid")
                total += i



    print_c(total)
    if autosubmit:
        submit(total,part="b", day=DAY, year=YEAR)


def parse_data(indata = None):
    if not indata:
        indata = open('data/2.in', 'r')
    lines = [l.strip() for l in indata]
    return lines[0].split(",")


if __name__ == '__main__':
    data = parse_data()
    data_real = parse_data(get_data(day=DAY, year=YEAR).splitlines(True))

    autosubmit = len(argv) >= 3 and argv[2] == 's'

    if len(argv) < 2 or argv[1] != '2':
        print("Part1 test:")
        solve(data, test=True)
        print("Part1: ")
        solve(data_real, autosubmit=autosubmit)
    else:
        print("Part2 test:")
        solve2(data, test=True)
        print("Part2: ")
        solve2(data_real, autosubmit=autosubmit)