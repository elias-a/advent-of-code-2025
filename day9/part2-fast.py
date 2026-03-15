from itertools import pairwise, combinations
from collections import defaultdict
from tqdm import tqdm


def get_area(pair):
    (x1, y1), (x2, y2) = pair
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


with open("input.txt", "rt") as f:
    red = [tuple(map(int, row.strip().split(","))) for row in f]

border = []
border_x = defaultdict(set)
border_y = defaultdict(set)
last = red[0]
for current in red[1:] + [red[0]]:
    border_x[current[0]].add(current[1])
    border_y[current[1]].add(current[0])

    if current[0] == last[0]:
        sign = int((current[1] - last[1]) / abs(current[1] - last[1]))
        for y in range(last[1]+sign*1, current[1], sign):
            border.append((current[0], y))
            border_x[current[0]].add(y)
            border_y[y].add(current[0])
    elif current[1] == last[1]:
        sign = int((current[0] - last[0]) / abs(current[0] - last[0]))
        for x in range(last[0]+sign*1, current[0], sign):
            border.append((x, current[1]))
            border_x[x].add(current[1])
            border_y[current[1]].add(x)

    border.append(current)
    last = current

"""
for x in border_x:
    border_x[x] = sorted(border_x[x])
for y in border_y:
    border_y[y] = sorted(border_y[y])
"""

"""
tile = min(border, key=lambda z: z[0])
index = border.index(tile)
traversal = border[index:] + border[:index]
"""

normals = defaultdict(set)
for tile1, tile2 in pairwise(border + [border[0]]):
    if tile1[0] == tile2[0]:
        if tile2[1] < tile1[1]:
            normals[tile1].add((-1, 0))
            normals[tile2].add((-1, 0))
        else:
            normals[tile1].add((1, 0))
            normals[tile2].add((1, 0))
    elif tile1[1] == tile2[1]:
        if tile2[0] > tile1[0]:
            normals[tile1].add((0, 1))
            normals[tile2].add((0, 1))
        else:
            normals[tile1].add((0, -1))
            normals[tile2].add((0, -1))

area = 0
options = sorted(combinations(red, 2), key=get_area, reverse=True)
for pair in tqdm(options):
    (x1, y1), (x2, y2) = pair
    rect_border = set()
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    is_valid = True

    horizontal = set(range(min_x+1, max_x))
    horizontal_normals = {(-1, 0), (1, 0)}

    if (min_x, min_y) not in normals:
        top_left_x = max({x for x in border_y[min_y] if x < min_x}, default=None)
        if top_left_x is None:
            # If `top_left_x` is None, there is no left border so
            # this shape is invalid.
            continue
        elif (
            (1, 0) in normals[top_left_x, min_y] and
            (-1, 0) not in normals[top_left_x, min_y]
        ):
            continue

    if (max_x, min_y) not in normals:
        top_right_x = min({x for x in border_y[min_y] if x > max_x}, default=None)
        if top_right_x is None:
            continue
        elif (
            (-1, 0) in normals[top_right_x, min_y] and
            (1, 0) not in normals[top_right_x, min_y]
        ):
            continue

    top = horizontal & border_y[min_y]
    for x in top:
        if (x, min_y) in normals:
            continue

        if len(horizontal_normals.difference(normals[x, min_y])) == 1:
            is_valid = False
            break

    if not is_valid:
        continue

    if (min_x, max_y) not in normals:
        bottom_left_x = max({x for x in border_y[max_y] if x < min_x}, default=None)
        if bottom_left_x is None:
            continue
        elif (
            (1, 0) in normals[bottom_left_x, max_y] and
            (-1, 0) not in normals[bottom_left_x, max_y]
        ):
            continue

    if (max_x, max_y) not in normals:
        bottom_right_x = min({x for x in border_y[max_y] if x > max_x}, default=None)
        if bottom_right_x is None:
            continue
        elif (
            (-1, 0) in normals[bottom_right_x, max_y]
            and (1, 0) not in normals[bottom_right_x, max_y]
        ):
            continue

    bottom = horizontal & border_y[max_y]
    for x in bottom:
        if (x, max_y) in normals:
            continue

        if len(horizontal_normals.difference(normals[x, max_y])) == 1:
            is_valid = False
            break

    if not is_valid:
        continue

    vertical = set(range(min_y+1, max_y))
    vertical_normals = {(0, -1), (0, 1)}

    if (min_x, min_y) not in normals:
        left_top_y = {y for y in border_x[min_x] if y < min_y}
        if len(left_top_y) == 0:
            continue
        left_top_y_border = max(left_top_y)

        if (0, -1) in normals[min_x, left_top_y_border]:
            continue

    if (min_x, max_y) not in normals:
        left_bottom_y = {y for y in border_x[min_x] if y > max_y}
        if len(left_bottom_y) == 0:
            continue
        left_bottom_y_border = min(left_bottom_y)

        if (0, 1) in normals[min_x, left_bottom_y_border]:
            continue

    left = vertical & border_x[min_x]
    for y in left:
        if (min_x, y) in normals:
            continue

        if len(vertical_normals.difference(normals[min_x, y])) == 1:
            is_valid = False
            break

    if not is_valid:
        continue

    if (max_x, min_y) not in normals:
        right_top_y = {y for y in border_x[max_x] if y < min_y}
        if len(right_top_y) == 0:
            continue
        right_top_y_border = max(right_top_y)

        if (0, -1) in normals[max_x, right_top_y_border]:
            continue

    if (max_x, max_y) not in normals:
        right_bottom_y = {y for y in border_x[max_x] if y > max_y}
        if len(right_bottom_y) == 0:
            continue
        right_bottom_y_border = min(right_bottom_y)

        if (0, 1) in normals[max_x, right_bottom_y_border]:
            continue

    right = vertical & border_x[max_y]
    for y in right:
        if (max_x, y) in normals:
            continue

        if len(vertical_normals.difference(normals[max_x, y])) == 1:
            is_valid = False
            break

    if not is_valid:
        continue

    if is_valid:
        area = get_area(pair)
        break

print(area)
