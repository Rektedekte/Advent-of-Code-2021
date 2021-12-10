from statistics import median

with open("input.txt", "r") as f:
    lines = f.read().split("\n")


delim_map = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

score_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

new_lines = [line for line in lines]
sub_scores = []

for i, line in enumerate(lines):
    opened = []
    valid = True

    for j, char in enumerate(line):
        if char in delim_map:
            opened.append(char)
        else:
            if char == delim_map[opened[-1]]:
                opened.pop(-1)
            else:
                valid = False
                break

    if valid:
        ending = "".join(delim_map[char] for char in reversed(opened))
        sub_score = 0

        for char in ending:
            sub_score *= 5
            sub_score += score_map[char]

        sub_scores.append(int(sub_score))

print(median(sub_scores))
