with open("input.txt", "rt") as f:
    rolls = set()
    for i, row in enumerate(f):
        for j, loc in enumerate(row.strip()):
            if loc == "@":
                rolls.add((i, j))

accessible = 0
while True:
    stop = True

    for i, j in rolls.copy():
        neighbors = {
            (i, j-1),
            (i-1, j-1),
            (i-1, j),
            (i-1, j+1),
            (i, j+1),
            (i+1, j+1),
            (i+1, j),
            (i+1, j-1),
        }
        num_neighbors = [n in rolls for n in neighbors].count(True)
        if num_neighbors < 4:
            accessible += 1
            rolls.remove((i, j))
            stop = False

    if stop:
        break

print(accessible)
