class Fish:
    def __init__(self, cycle=8):
        self.cycle = cycle

    def __str__(self):
        return str(self.cycle)

    def __repr__(self):
        return str(self.cycle)

    def tick(self):
        self.cycle -= 1

    def will_spawn(self):
        if self.cycle < 0:
            self.cycle = 6
            return True

def simulate(fishes, days, cache=None):
    save_cache = True
    if cache is None:
        save_cache = False

    for i in range(1, days - 8):
        new = []

        for fish in fishes:
            fish.tick()

            if fish.will_spawn():
                new.append(Fish())

        fishes += new

    for i in range(days - 8, days + 1):
        new = []

        for fish in fishes:
            fish.tick()

            if fish.will_spawn():
                new.append(Fish())

        fishes += new

        if save_cache:
            cache[i] = [fish.cycle for fish in fishes]


sub_length = 128
cache = {}
simulate([Fish(0)], sub_length, cache)
print(cache)


with open("input.txt", "r") as f:
    data = f.read()

fishes_in = map(int, data.split(","))
fishes = []

for fish_in in fishes_in:
    fishes.append(Fish(fish_in))

c = 0

for fish in fishes:
    sub_products = cache[sub_length - fish.cycle]

    for sub_product in sub_products:
        c += len(cache[sub_length - sub_product])

print(c)
