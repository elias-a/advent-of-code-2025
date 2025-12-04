with open("input.txt", "rt") as f:
    banks = []
    for bank in f:
        banks.append([int(b) for b in bank.strip()])

total_joltage = 0
for bank in banks:
    remaining_bank = bank
    digits = ""

    while len(digits) < 12:
        num_remaining = 12 - len(digits)

        if num_remaining > 1:
            options = remaining_bank[:-num_remaining+1]
        else:
            options = remaining_bank

        index = remaining_bank.index(max(options))
        digits += str(remaining_bank[index])
        remaining_bank = remaining_bank[index+1:]

    total_joltage += int(digits)

print(total_joltage)
