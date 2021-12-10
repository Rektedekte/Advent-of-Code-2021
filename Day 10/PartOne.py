with open("input.txt", "r") as f:
    lines = f.read().split("\n")


delim_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

score_map = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

c = 0

for i, line in enumerate(lines):
    opened = []

    for j, char in enumerate(line):
        if char in delim_map:
            opened.append(char)
        else:
            if char == delim_map[opened[-1]]:
                opened.pop(-1)
            else:
                c += score_map[char]
                break

print(c)
