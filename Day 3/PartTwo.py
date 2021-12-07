def get_lines():
    with open("input.txt", "r") as f:
        return f.read().split("\n")


def partial(i, flip):
    c = 0

    for line in lines:
        if line[i] == "1":
            c += 1

    return str(int(c >= len(lines) / 2) ^ flip)


def filter_from_crit(i, crit):
    global lines
    new_lines = []

    for line in lines:
        if line[i] == crit:
            new_lines.append(line)

    lines = new_lines


lines = get_lines()

for i in range(12):
    crit = partial(i, 0)
    filter_from_crit(i, crit)

oxy_byte = "".join(lines[0])

lines = get_lines()

for i in range(12):
    crit = partial(i, 1)
    filter_from_crit(i, crit)

    if len(lines) == 1:
        break

scrub_byte = "".join(lines[0])

OXY = int(oxy_byte, 2)
CO2 = int(scrub_byte, 2)

print(OXY * CO2)
