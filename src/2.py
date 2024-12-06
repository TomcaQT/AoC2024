from collections import Counter

def is_save(x):
    diff = [x[i] - x[i+1] for i in range(len(x)-1) ]

    if not all(d < 0 for d in diff) and not all(d > 0 for d in diff):
        return False
    if any(abs(d) > 3 for d in diff):
        return False
    return True

def solve(data):
    total = 0
    for x in data:
        if is_save(x):
            total += 1
    print(total)

def solve2(data):
    total = 0
    for x in data:
        for i in range(len(x)):
            new_x = x[0:i] + x[i+1:]
            if is_save(new_x):
                total += 1
                break
    print(total)


def read_file():
    data = []
    with open('data/2.in', 'r') as f:
        for l in f.readlines():
            data.append(list(map(int, l.split())))
        return data


if __name__ == '__main__':
    data = read_file()
    solve(data)
    solve2(data)