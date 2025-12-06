from operator import mul
from functools import reduce


with open("input.txt", "rt") as f:
    data = [list(row.strip("\n")) for row in f]

total = 0
operands = []
for j in range(len(data[0])-1, -1, -1):
    col = [data[i][j] for i in range(len(data))]

    if all(c == " " for c in col):
        continue

    num = int("".join([c for c in col[:-1] if c != " "]))
    op = col[-1]
    operands.append(num)

    if op == "+":
        total += sum(operands)
        operands = []
    elif op == "*":
        total += reduce(mul, operands)
        operands = []

print(total)
