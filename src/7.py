from collections import Counter
from aocd import get_data
from itertools import combinations_with_replacement, product

def solve(data, test=False):
    if test:
        print(data)
        total = 0
        for eq in data:
            res, vals = int(eq[0]), list(map(int,eq[1].strip().split()))
            comb = list(product(["+", "*"], repeat=len(vals)-1))
            #print(f"{res}={vals} try {comb}")

            for c in comb:
                v = vals[0]
                for val, op in zip(vals[1:], c):
                    if op == "+":
                        v += val
                    else:
                        v *= val
                #print(f"{v=}")
                if res == v:
                    total += res
                    break
        print(total)





def solve2(data, test=False):
    total = 0
    for eq in data:
        res, vals = int(eq[0]), list(map(int,eq[1].strip().split()))
        comb = list(product(["+", "*", "I"], repeat=len(vals)-1))
        #print(f"{res}={vals} try {comb}")

        for c in comb:
            v = vals[0]
            for val, op in zip(vals[1:], c):
                if op == "+":
                    v += val
                elif op == "*":
                    v *= val
                else:
                    v = int(str(v) + str(val))
            #print(f"{v=}")
            if res == v:
                total += res
                break
    print(total)


def read_file():
    data = []
    with open('../data/7.in', 'r') as f:
        return [list(l.split(':'))for l in f.readlines()]


if __name__ == '__main__':
    data = read_file()
    print("Testing data: ")
    solve(data, test=True)
    solve2(data, test=True)
