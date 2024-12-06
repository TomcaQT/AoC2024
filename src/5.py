from collections import Counter, defaultdict
from aocd import get_data

def check_update(update, rules):

    prev = []
    for u in update:
        for p in prev:
            if p in rules[u]:
                return False
        prev.append(u)
    return True



def solve(data, test=False):
    rules = data[0]
    updates = data[1]
    total = 0
    inc = []
    for update in updates:
        if check_update(update, rules):
            total += update[len(update)//2]
        else:
            inc.append(update)

    print(total)
    return inc

def solve2(data, updates):
    rules = data[0]
    total = 0
    for nums in updates:
        orignums = nums[:]
        badone = True
        while badone:
            badone = False
            for i in range(1, len(nums)):
                if not nums[i] in rules[nums[i-1]]:
                    nums[i], nums[i-1] = nums[i-1], nums[i]
                    badone = True
        if not orignums == nums:
            total += nums[len(nums)//2]

    print(total)



def read_file():
    rules = defaultdict(set)
    updates = []
    with open('../data/5.in', 'r') as f:
        for line in f:
            line = line.strip()
            if '|' in line:
                x,y = line.split('|')
                rules[int(x)].add(int(y))
            if ',' in line:
                updates.append(list(map(int,line.split(','))))
    return [rules, updates]


if __name__ == '__main__':
    data = read_file()
    print("Testing data: ")
    incorrect = solve(data, test=True)
    solve2(data, incorrect)
