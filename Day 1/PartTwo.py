c = 0

with open("../BiggerThanSum/input.txt", "r") as f:
    prev = 9999
    lines = list(map(int, f.readlines()))

    for i in range(len(lines) - 2):
        sum_lines = sum(lines[i: i+3])
        print(sum_lines)

        if sum_lines > prev:
            c += 1

        prev = sum_lines

print(c)
