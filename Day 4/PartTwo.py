import numpy as np


class Board:
    def __init__(self, board):
        self.nums = np.array(board.split(" "), dtype=int)
        self.nums.shape = (5, 5)
        self.marked = np.zeros((5, 5), bool)

    def mark(self, n):
        for i in range(5):
            for j in range(5):
                if self.nums[i, j] == n:
                    self.marked[i, j] = True

    def get_match(self):
        for val in np.sum(self.marked, axis=0):
            if val == 5:
                return True

        for val in np.sum(self.marked, axis=1):
            if val == 5:
                return True

        return False

    def get_sum(self):
        c = 0

        for i in range(5):
            for j in range(5):
                if not self.marked[i, j]:
                    c += self.nums[i, j]

        return c


with open("input.txt", "r") as f:
    lines = f.read().split("\n")

nums = [int(n) for n in lines[0].split(",")]

boards = []

for i in range(2, len(lines), 6):
    board_lines = []

    for j in range(i, i + 5):
        board_lines.append(lines[j])

    board_con = " ".join(board_lines)
    board_con = board_con.replace("  ", " ").lstrip(" ")
    boards.append(Board(board_con))

for num in nums:
    new_boards = []

    for i, board in enumerate(boards):
        board.mark(num)

        if board.get_match():
            s = board.get_sum()
            print(s * num)
            del board

        else:
            new_boards.append(board)

    boards = new_boards
