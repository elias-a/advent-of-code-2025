from itertools import batched


with open("input.txt", "rt") as f:
    ranges = f.read().strip().split(",")

sum_invalids = 0
for r in ranges:
    start, end = (int(n) for n in r.split("-"))
    for num in range(start, end+1):
        s_num = str(num)

        for n in range(1, len(s_num)):
            if len(s_num) % n != 0:
                continue

            batches = batched(s_num, n=n)
            first = next(batches)
            if all(b == first for b in batches):
                sum_invalids += int(s_num)
                break

print(sum_invalids)
