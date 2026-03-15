from itertools import pairwise, combinations
from collections import defaultdict


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

for x in border_x:
    border_x[x] = sorted(border_x[x])
for y in border_y:
    border_y[y] = sorted(border_y[y])

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


validity = {}


calls = 0


def check_point(point_x, point_y):
    global calls
    calls += 1
    if (point_x, point_y) in normals:
        return True

    if (point_x, point_y) in normals and normals[point_x, point_y] is True:
        return True

    right_x = None
    for i in range(len(border_y[point_y])-1, 0, -1):
        if border_y[point_y][i-1] < point_x:
            right_x = border_y[point_y][i]
            break
    """
    for xp in border_y[point_y]:
        if xp > point_x:
            right_x = xp
            break
    """
    #right_x = next((xp for xp in border_y[point_y] if xp > point_x), None)

    if right_x is None:
        validity[point_x, point_y] = False
        return False

    if (-1, 0) in normals[(right_x, point_y)]:
        validity[point_x, point_y] = False
        return False

    right_index = border_y[point_y].index(right_x)
    if right_index == 0:
        validity[point_x, point_y] = False
        return False

    left_x = border_y[point_y][right_index-1]
    if (1, 0) in normals[(left_x, point_y)]:
        validity[point_x, point_y] = False
        return False

    bottom_y = None
    for yp in border_x[point_x]:
        if yp > point_y:
            bottom_y = yp
            break
    #bottom_y = next((yp for yp in border_x[point_x] if yp > point_y), None)
    if bottom_y is None:
        validity[point_x, point_y] = False
        return False

    if (0, 1) in normals[(point_x, bottom_y)]:
        validity[point_x, point_y] = False
        return False

    bottom_index = border_x[point_x].index(bottom_y)
    if bottom_index == 0:
        validity[point_x, point_y] = False
        return False

    upper_y = border_x[point_x][bottom_index-1]
    if (0, -1) in normals[(point_x, upper_y)]:
        validity[point_x, point_y] = False
        return False

    validity[point_x, point_y] = True
    return True


area = 0
options = sorted(combinations(red, 2), key=get_area, reverse=True)
count = 0
points = []
for pair in options:
    print(calls)
    it_points = set()
    count += 1

    if count > 10:
        break

    (x1, y1), (x2, y2) = pair
    rect_border = set()
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    is_valid = True

    for x in range(min_x, max_x+1):
        it_points.add((x, min_y))
        if not check_point(x, min_y):
            is_valid = False
            break

        it_points.add((x, max_y))
        if not check_point(x, max_y):
            is_valid = False
            break

    if not is_valid:
        points.append(it_points)
        continue

    for y in range(min_y, max_y+1):
        it_points.add((min_x, y))
        if not check_point(min_x, y):
            is_valid = False
            break

        it_points.add((max_x, y))
        if not check_point(max_x, y):
            is_valid = False
            break

    if not is_valid:
        points.append(it_points)
        continue

    if is_valid:
        area = get_area(pair)
        break

    points.append(it_points)


#print(area)
