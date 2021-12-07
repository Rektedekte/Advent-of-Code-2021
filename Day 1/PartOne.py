c = 0

with open("input.txt", "r") as f:
    prev = 9999

    for line in f.readlines():
        if int(line) > prev:
            c += 1

        prev = int(line)

print(c)
