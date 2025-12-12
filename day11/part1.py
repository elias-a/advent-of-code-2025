with open("input.txt", "rt") as f:
    rows = [row.strip() for row in f]

output_map = {}
for row in rows:
    device, outputs = [x.strip() for x in row.split(":")]
    output_map[device] = outputs.split(" ")

num_paths = 0
devices = ["you"]
while len(devices) > 0:
    next_devices = []
    for current in devices.copy():
        for output in output_map[current]:
            if output == "out":
                num_paths += 1
                continue
            else:
                next_devices.append(output)

    devices = next_devices

print(num_paths)
