from collections import Counter
from aocd import get_data

def solve(data, test=False):
    space, id = False, 0
    mem = []
    for n in data:
        n = int(n)
        if space:
            mem += "." * n
        else:
            mem += [str(id) for _ in range(n)]
            id += 1

        space = not space

    s, e = 0, len(mem) - 1
    while s <= e:
        while mem[s] != ".":
            s += 1
        while mem[e] == ".":
            e -= 1
        if s >= e:
            break
        mem[s], mem[e] = mem[e], mem[s]
        s += 1
        e -= 1
    total = 0
    for i,x in enumerate(mem):
        if x == ".":
            break
        else:
            total += int(x) * i
    print(total)



def solve2(data, test=False):
    space, id = False, 0
    mem = []
    for n in data:
        n = int(n)
        if space:
            mem += "." * n
        else:
            mem += [str(id) for _ in range(n)]
            id += 1

        space = not space

    e, ee = len(mem) - 1, len(mem) - 1
    while e > 0:
        s, ss = 0, 0
        while mem[e] == ".":
            if e < 0:
                break
            e -= 1
        while mem[s] != ".":
            s += 1


        mem[s], mem[e] = mem[e], mem[s]
        s += 1
        e -= 1
    total = 0
    for i,x in enumerate(mem):
        if x == ".":
            break
        else:
            total += int(x) * i
    print(total)


def read_file():
    data = []
    with open('data/9.in', 'r') as f:
        return f.readlines()[0].strip()


if __name__ == '__main__':
    data = read_file()
    print("Testing data: ")
    #solve(data, test=True)
    solve2(data, test=True)
