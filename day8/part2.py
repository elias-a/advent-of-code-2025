from math import sqrt
from collections import defaultdict


with open("input.txt", "rt") as f:
    positions = [tuple(map(int, pos.strip().split(","))) for pos in f]

distances = {}
for pos in positions:
    x, y, z = pos
    for other_pos in positions:
        if pos == other_pos:
            continue
        elif (pos, other_pos) in distances or (other_pos, pos) in distances:
            continue
        xp, yp, zp = other_pos
        distance = sqrt((x-xp)**2 + (y-yp)**2 + (z-zp)**2)
        distances[pos, other_pos] = distance

sorted_distances = sorted(distances.items(), key=lambda d: d[-1])

answer = 0
circuits = defaultdict(set)
for (box1, box2), _ in sorted_distances:
    box1_existing = circuits[box1]
    box2_existing = circuits[box2]
    new_circuit = {box1, box2} | box1_existing | box2_existing
    for c in new_circuit:
        circuits[c] = new_circuit

    if len(circuits[box1]) == len(positions):
        answer = box1[0] * box2[0]
        break

print(answer)
