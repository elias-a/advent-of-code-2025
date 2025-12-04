with open("input.txt", "rt") as f:
    banks = []
    for bank in f:
        banks.append([int(b) for b in bank.strip()])

total_joltage = 0
for bank in banks:
    first_index = bank.index(max(bank[:-1]))
    second_index = bank.index(max(bank[first_index+1:]))
    max_joltage = bank[first_index] * 10 + bank[second_index]
    total_joltage += max_joltage

print(total_joltage)
