

with open("input.txt", "rt") as f:
    ranges = f.read().strip().split(",")

sum_invalids = 0
for r in ranges:
    start, end = (int(n) for n in r.split("-"))
    for num in range(start, end+1):
        s_num = str(num)

        if len(s_num) % 2 != 0:
            continue

        half_length = len(s_num) // 2
        if all(s_num[i] == s_num[i+half_length] for i in range(half_length)):
            sum_invalids += int(s_num)

print(sum_invalids)
