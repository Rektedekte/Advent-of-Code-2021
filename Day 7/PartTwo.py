from statistics import mean
from math import floor

with open("input.txt", "r") as f:
    data = f.read()

def calculateFuel(med):
    c = 0

    for crab in crabs:
        diff = abs(crab - med)
        c += (diff**2 + diff) // 2

    return c


crabs = list(map(int, data.split(",")))
m = floor(mean(crabs))

print(calculateFuel(m))
