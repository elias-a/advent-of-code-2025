with open("input.txt", "rt") as f:
    manifold = [list(row.strip()) for row in f]

s = manifold[0].index("S")
active = {(1, s)}
timelines = {(1, s): 1}

num_timelines = 0
while len(active) > 0:
    for i, j in active.copy():
        active.remove((i, j))
        count = timelines.pop((i, j))
        next_i, next_j = (i+1, j)

        if next_i >= len(manifold):
            num_timelines += count
            continue
        elif manifold[next_i][next_j] == "^":
            left = (next_i, j-1)
            if left in active:
                timelines[left] += count
            else:
                active.add(left)
                timelines[left] = count

            right = (next_i, j+1)
            if right in active:
                timelines[right] += count
            else:
                active.add(right)
                timelines[right] = count
        else:
            next_coord = (next_i, next_j)
            if next_coord in active:
                timelines[next_coord] += count
            else:
                active.add(next_coord)
                timelines[next_coord] = count

print(num_timelines)
