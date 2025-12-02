

with open("input.txt", "rt") as f:
    rotations = [row.strip() for row in f]

num_zero = 0
dial = 50
for rot in rotations:
    direction, clicks = rot[0], int(rot[1:])
    full_rot = clicks // 100
    rem = clicks % 100

    num_zero += full_rot

    if direction == "L":
        if rem > 0 and dial > 0 and rem >= dial:
            num_zero += 1
        dial = (dial - rem) % 100
    elif direction == "R":
        if rem > 0 and dial > 0 and rem >= (100 - dial):
            num_zero += 1
        dial = (dial + rem) % 100

print(num_zero)
