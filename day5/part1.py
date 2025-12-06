with open("input.txt", "rt") as f:
    s_ranges, s_ingredients = f.read().strip().split("\n\n")

ranges = set()
for r in s_ranges.strip().split("\n"):
    start, stop = map(int, r.split("-"))
    ranges.add(range(start, stop+1))

num_fresh = 0
for s_ingredient in s_ingredients.strip().split("\n"):
    if any(int(s_ingredient) in r for r in ranges):
        num_fresh += 1

print(num_fresh)
