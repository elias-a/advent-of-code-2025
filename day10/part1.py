with open("input.txt", "rt") as f:
    machines = [row.strip().split(" ") for row in f]

answer = 0
for machine in machines:
    diagram, *buttons, _ = machine

    s_diagram = "".join("1" if x == "#" else "0" for x in diagram[1:-1])
    diagram_num = int(s_diagram, 2)

    button_nums = []
    for button in buttons:
        nums = tuple(map(int, button[1:-1].split(",")))
        s_button = "".join("1" if i in nums else "0"
                           for i in range(len(s_diagram)))
        button_nums.append(int(s_button, 2))

    results = [int("".join("0" for _ in range(len(s_diagram))), 2)]
    depth = 0
    while True:
        next_level = []
        for r in results.copy():
            for b in button_nums:
                next_level.append(b ^ r)

        results = next_level
        depth += 1

        if any(r == diagram_num for r in results):
            break

    answer += depth

print(answer)
