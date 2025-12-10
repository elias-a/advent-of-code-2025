from itertools import pairwise, combinations


def get_area(pair):
    (x1, y1), (x2, y2) = pair
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


with open("ex.txt", "rt") as f:
    red = [tuple(map(int, row.strip().split(","))) for row in f]

border = set()
for tile1, tile2 in pairwise(red + [red[0]]):
    border.add(tile1)
    border.add(tile2)

    if tile1[0] == tile2[0]:
        min_y = min(tile1[1], tile2[1])
        max_y = max(tile1[1], tile2[1])
        for y in range(min_y+1, max_y):
            border.add((tile1[0], y))
    elif tile1[1] == tile2[1]:
        min_x = min(tile1[0], tile2[0])
        max_x = max(tile1[0], tile2[0])
        for x in range(min_x+1, max_x):
            border.add((x, tile1[1]))

answer = 0
options = sorted(combinations(red, 2), key=get_area, reverse=True)
for pair in options:
    (x1, y1), (x2, y2) = pair
    tile3 = (x1, y2)
    tile4 = (x2, y1)
    if tile3 in border and tile4 in border:
        answer = get_area(pair)
        break

print(answer)
