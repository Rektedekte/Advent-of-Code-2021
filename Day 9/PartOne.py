import numpy as np

def get_surrounding(i, j):
    neigh = []

    if i + 1 < h:
        neigh.append((i + 1, j))
    if i - 1 >= 0:
        neigh.append((i - 1, j))
    if j + 1 < w:
        neigh.append((i, j + 1))
    if j - 1 >= 0:
        neigh.append((i, j - 1))

    return neigh


with open("input.txt", "r") as f:
    lines = f.read().split("\n")

w = len(lines[0])
h = len(lines)
buffer = "".join(lines)

arr = np.fromiter(buffer, dtype="uint8")
arr.shape = (h, w)
c = 0

for i in range(h):
    for j in range(w):
        is_hole = True

        for k, l in get_surrounding(i, j):
            if arr[k, l] <= arr[i, j]:
                is_hole = False

        if is_hole:
            c += arr[i, j] + 1

print(c)
