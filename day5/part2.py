with open("input.txt", "rt") as f:
    s_ranges, _ = f.read().strip().split("\n\n")

ranges = []
for r in s_ranges.strip().split("\n"):
    start, stop = map(int, r.split("-"))
    candidates = [range(start, stop+1)]

    for r in ranges:
        for candidate in candidates.copy():
            candidates.remove(candidate)
            start, stop = candidate.start, candidate.stop-1

            if stop < r.start or start >= r.stop:
                candidates.append(candidate)
            elif start < r.start and stop >= r.stop:
                candidates.append(range(start, r.start))
                candidates.append(range(r.stop, stop+1))
            elif start < r.start and stop in r:
                candidates.append(range(start, r.start))
            elif start in r and stop >= r.stop:
                candidates.append(range(r.stop, stop+1))

    ranges.extend(candidates)

num_fresh = sum(len(r) for r in ranges)
print(num_fresh)
