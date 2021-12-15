class Path:
    def __init__(self, curr, exclude, two_ex):
        self.curr = curr
        self.exclude = [item for item in exclude]
        self.two_ex = two_ex

        if not size_dict[self.curr]:
            self.exclude.append(self.curr)

    def create_new(self):
        paths = []

        for new in nav_paths[self.curr]:
            if new not in self.exclude:
                new_path = Path(new, self.exclude, self.two_ex)
                paths.append(new_path)
            else:
                if not self.two_ex and new not in {"start", "end"}:  # Two trigger has not been used
                    new_path = Path(new, self.exclude, True)
                    paths.append(new_path)

        return paths


with open("input.txt", "r") as f:
    data = f.read().split("\n")

nav_paths = {}
size_dict = {}

for line in data:
    a, b = line.split("-")

    if a not in nav_paths:
        nav_paths[a] = []

    nav_paths[a].append(b)

    if b not in nav_paths:
        nav_paths[b] = []

    nav_paths[b].append(a)

    size_dict[a] = 64 < ord(a[0]) < 91
    size_dict[b] = 64 < ord(b[0]) < 91


paths = []
new = [Path("start", [], False)]
done = []

while new:
    paths = [item for item in new]
    new.clear()

    for path in paths:
        if path.curr == "end":
            done.append(path)
        else:
            new.extend(path.create_new())

print(len(done))
