import numpy as np

w = 1350
h = 1350

with open("input.txt", "r") as f:
    data = f.read()

p1, p2 = data.split("\n\n")
grid = np.zeros((h, w), dtype=bool)

for line in p1.split("\n"):
    x, y = line.split(",")
    x = int(x)
    y = int(y)

    grid[y, x] = 1

direc, coord = p2.split("\n")[0].lstrip("fold along ").split("=")
coord = int(coord)

if direc == "x":
    for i in range(h):
        for j in range(coord + 1, w):
            if grid[i, j]:
                grid[i, 2 * coord - j] = 1

    grid = grid[0: h, 0: coord]

else:
    for i in range(coord + 1, h):
        for j in range(w):
            if grid[i, j]:
                grid[2 * coord - i, j] = 1

    grid = grid[0: coord]


print(np.sum(grid))
