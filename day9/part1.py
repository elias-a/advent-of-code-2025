from itertools import combinations


with open("input.txt", "rt") as f:
    red = [tuple(map(int, row.strip().split(","))) for row in f]

area = max((abs(x1-x2) + 1) * (abs(y1-y2) + 1)
           for (x1, y1), (x2, y2) in combinations(red, 2))
print(area)
