with open("input.txt", "r") as f:
    data = f.read()

chain, p2 = data.split("\n\n")
chain = list(chain)
pair_inser = {item.split(" -> ")[0]: item.split(" -> ")[1] for item in p2.split("\n")}

for _ in range(20):
    i = 0

    while i < len(chain) - 1:
        pair = "".join(chain[i: i + 2])

        if pair in pair_inser:
            chain.insert(i + 1, pair_inser[pair])
            i += 1

        i += 1


pop_dict = {}

for elem in chain:
    if elem not in pop_dict:
        pop_dict[elem] = 0

    pop_dict[elem] += 1


elems = list(pop_dict.keys())
elems.sort(key=lambda elem: pop_dict[elem])

print(pop_dict[elems[-1]] - pop_dict[elems[0]])
