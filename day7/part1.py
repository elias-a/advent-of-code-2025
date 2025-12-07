with open("input.txt", "rt") as f:
    manifold = [list(row.strip()) for row in f]

s = manifold[0].index("S")
tachyons = {(1, s)}

num_split = 0
while len(tachyons) > 0:
    for i, j in tachyons.copy():
        tachyons.remove((i, j))
        next_i, next_j = (i+1, j)

        if next_i >= len(manifold):
            continue
        elif manifold[next_i][next_j] == "^":
            tachyons.add((next_i, j-1))
            tachyons.add((next_i, j+1))
            num_split += 1
        else:
            tachyons.add((next_i, next_j))

print(num_split)
