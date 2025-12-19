import pulp as pl


with open("input.txt", "rt") as f:
    machines = [row.strip().split(" ") for row in f]

answer = 0
for machine in machines:
    _, *s_buttons, s_counters = machine
    buttons = [tuple(map(int, b[1:-1].split(","))) for b in s_buttons]
    target = list(map(int, s_counters[1:-1].split(",")))

    model = pl.LpProblem("Buttons", pl.LpMinimize)

    vars = []
    constraint = ()
    for i in range(len(buttons)):
        var = pl.LpVariable("x"+str(i), lowBound=0, cat="Integer")
        vars.append(var)
        constraint += var

    model += constraint

    for i, t in enumerate(target):
        action = ()
        for v, b in zip(vars, buttons):
            if i in b:
                action += v
        model += action == t

    model.solve(pl.PULP_CBC_CMD(msg=False))

    answer += int(sum(pl.value(v) for v in vars))

print(answer)
