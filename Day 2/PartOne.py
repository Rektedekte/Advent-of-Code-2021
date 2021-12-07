x = 0
y = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        direc, offset = line.split(" ")
        offset = int(offset)

        if direc == "forward":
            x += offset

        elif direc == "up":
            y -= offset

        elif direc == "down":
            y += offset

print(x * y)
