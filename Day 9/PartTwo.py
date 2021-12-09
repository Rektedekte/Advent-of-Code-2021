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

def get_basin_size(i, j):
    new = [(i, j)]
    collected = []

    while new:
        collected.extend(new)
        new.clear()

        for k, l in collected:
            for n, m in get_surrounding(k, l):
                if (n, m) not in collected and (n, m) not in new:
                    if arr[n, m] != 9:
                        new.append((n, m))

    return len(collected)


with open("input.txt", "r") as f:
    lines = f.read().split("\n")

w = len(lines[0])
h = len(lines)
buffer = "".join(lines)

arr = np.fromiter(buffer, dtype="uint8")
arr.shape = (h, w)

low_points = []

for i in range(h):
    for j in range(w):
        is_hole = True

        for k, l in get_surrounding(i, j):
            if arr[k, l] <= arr[i, j]:
                is_hole = False

        if is_hole:
            low_points.append((i, j))


largest = [0, 0, 0]

for i, j in low_points:
    size = get_basin_size(i, j)

    if size > largest[0]:
        largest.pop(0)
        largest.append(size)
        largest = sorted(largest)

print(largest[0] * largest[1] * largest[2])
