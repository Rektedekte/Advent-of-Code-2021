with open("input.txt", "r") as f:
    con = f.read().split("\n")

lines = [(coords.split(" -> ")[0].split(","), coords.split(" -> ")[1].split(",")) for coords in con]
vent_map = [[0 for j in range(1000)] for i in range(1000)]

for (x1, y1), (x2, y2) in lines:
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    if x1 == x2:
        if y1 < y2:
            r = range(y1, y2 + 1)
        else:
            r = range(y2, y1 + 1)

        for i in r:
            vent_map[i][x1] += 1

    elif y1 == y2:
        if x1 < x2:
            r = range(x1, x2 + 1)
        else:
            r = range(x2, x1 + 1)

        for i in r:
            vent_map[y1][i] += 1

c = 0

for i in range(1000):
    for j in range(1000):
        if vent_map[i][j] > 1:
            c += 1

print(c)
