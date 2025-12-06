from operator import mul
from functools import reduce


with open("input.txt", "rt") as f:
    rows = [row.strip().split() for row in f]

total = 0
for j in range(len(rows[0])):
    problem = [rows[i][j] for i in range(len(rows))]
    nums = map(int, problem[:-1])
    op = problem[-1]

    if op == "+":
        total += sum(nums)
    elif op == "*":
        total += reduce(mul, nums)

print(total)
