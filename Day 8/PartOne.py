with open("input.txt", "r") as f:
    lines = map(lambda line: line.split("|")[1], f.read().split("\n"))

c = 0

for line in lines:
    for digit in line.split(" "):
        if len(digit) in {2, 4, 3, 7}:
            c += 1

print(c)
