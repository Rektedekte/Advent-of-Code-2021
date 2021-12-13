import numpy as np


w = 10
h = 10


class Grid:
    def __init__(self, board):
        self.nums = np.array(board.split(" "), dtype=int)
        self.nums.shape = (h, w)
        self.exclude = []
        self.c = 0

    def tick(self):
        for i in range(h):
            for j in range(w):
                self.nums[i, j] += 1

        self.check()
        self.exclude.clear()

    def get_bounds(self, i, j):
        return max(i - 1, 0), max(j - 1, 0), min(i + 2, h), min(j + 2, w)

    def flash(self, i, j):
        self.c += 1
        i_l, j_l, i_h, j_h = self.get_bounds(i, j)
        self.nums[i, j] = 0
        self.exclude.append((i, j))

        for k in range(i_l, i_h):
            for l in range(j_l, j_h):
                if (k != i or l != j) and (k, l) not in self.exclude:
                    self.nums[k, l] += 1

                    if self.nums[k, l] > 9:
                        self.flash(k, l)

    def check(self):
        for i in range(h):
            for j in range(w):
                if self.nums[i, j] > 9:
                    self.flash(i, j)


with open("input.txt", "r") as f:
    data = " ".join(char for char in "".join(f.read().split("\n")))


grid = Grid(data)


for i in range(100):
    grid.tick()


print(grid.c)
