""" Far too slow, not sure if it works """


from collections import defaultdict
from itertools import combinations


def get_area(pair):
    (x1, y1), (x2, y2) = pair
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


with open("input.txt", "rt") as f:
    red = [tuple(map(int, row.strip().split(","))) for row in f]

border = set()
border_x = defaultdict(list)
border_y = defaultdict(list)
last = red[0]
for current in red[1:] + [red[0]]:
    border.add(current)

    border_x[current[0]].append(current[1])
    border_y[current[1]].append(current[0])

    if current[0] == last[0]:
        min_y = min(current[1], last[1])
        max_y = max(current[1], last[1])
        for y in range(min_y+1, max_y):
            border.add((current[0], y))

            border_x[current[0]].append(y)
            border_y[y].append(current[0])
    elif current[1] == last[1]:
        min_x = min(current[0], last[0])
        max_x = max(current[0], last[0])
        for x in range(min_x+1, max_x):
            border.add((x, current[1]))

            border_x[x].append(current[1])
            border_y[current[1]].append(x)

    last = current

[border_x[x].sort() for x in border_x]
[border_y[y].sort() for y in border_y]

red_or_green = border.copy()


def is_in(x_tile, y_tile):
    y2 = next((y for y in border_x[x_tile] if y > y_tile), None)
    if y2 is None or y2 == border_x[x_tile][0]:
        return False
    y1 = border_x[x_tile][border_x[x_tile].index(y2)-1]

    x2 = next((x for x in border_y[y_tile] if x > x_tile), None)
    if x2 is None or x2 == border_y[y_tile][0]:
        return False
    x1 = border_y[y_tile][border_y[y_tile].index(x2)-1]

    if (
        # top is good
        all(border_x[x][0] < y_tile for x in range(x1+1, x_tile)) and
        # bottom is good
        all(border_x[x][-1] > y_tile for x in range(x_tile+1, x2)) and
        # left is good
        all(border_y[y][0] < x_tile for y in range(y1+1, y_tile)) and
        # right is good
        all(border_y[y][-1] > x_tile for y in range(y_tile+1, y2))
    ):
        return True
    else:
        return False


def check_pair(pair):
    (x1, y1), (x2, y2) = pair
    min_x, max_x = sorted((x1, x2))
    min_y, max_y = sorted((y1, y2))

    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            if (x, y) in red_or_green:
                continue
            elif is_in(x, y):
                red_or_green.add((x, y))
                continue
            else:
                return False

    return True


answer = 0
options = sorted(combinations(red, 2), key=get_area, reverse=True)
for pair in options:
    if check_pair(pair):
        answer = get_area(pair)
        break

print(answer)
