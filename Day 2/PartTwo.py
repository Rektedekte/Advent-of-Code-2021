x = 0
y = 0
aim = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        direc, offset = line.split(" ")
        offset = int(offset)

        if direc == "forward":
            x += offset
            y += aim * offset

        elif direc == "up":
            aim -= offset

        elif direc == "down":
            aim += offset

print(x * y)
