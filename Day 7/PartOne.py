from statistics import median

with open("input.txt", "r") as f:
    data = f.read()

def calculateFuel(med):
    c = 0

    for crab in crabs:
        c += abs(crab - med)

    return c


crabs = list(map(int, data.split(",")))
m = median(crabs)

print(calculateFuel(m))
