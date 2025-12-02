

with open("input.txt", "rt") as f:
    rotations = [row.strip() for row in f]

num_zero = 0
dial = 50
for rot in rotations:
    direction, clicks = rot[0], int(rot[1:])

    if direction == "L":
        dial = (dial - clicks) % 100
    elif direction == "R":
        dial = (dial + clicks) % 100

    if dial == 0:
        num_zero += 1

print(num_zero)
