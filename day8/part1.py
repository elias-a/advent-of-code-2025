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

max_connections = 1000
circuits = defaultdict(set)
for (box1, box2), _ in sorted_distances[:max_connections]:
    box1_existing = circuits[box1]
    box2_existing = circuits[box2]
    new_circuit = {box1, box2} | box1_existing | box2_existing
    for c in new_circuit:
        circuits[c] = new_circuit

unique = []
for c in circuits.values():
    if c not in unique:
        unique.append(c)

lengths = sorted(map(len, unique), reverse=True)
answer = lengths[0] * lengths[1] * lengths[2]
print(answer)
