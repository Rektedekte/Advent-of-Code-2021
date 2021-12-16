def cache_steps(chain, steps):
    for _ in range(steps):
        i = 0

        while i < len(chain) - 1:
            pair = "".join(chain[i: i + 2])

            if pair in pair_inser:
                chain.insert(i + 1, pair_inser[pair])
                i += 1

            i += 1

    chain = chain[1: -1]
    return chain


def get_count(chain):
    count = {k: 0 for k in all_bases}

    for elem in chain:
        count[elem] += 1

    return count


all_bases = ("N", "C", "B", "H", "P", "F", "S", "O", "V", "K")

with open("input.txt", "r") as f:
    data = f.read()

chain, p2 = data.split("\n\n")
pair_inser = {item.split(" -> ")[0]: item.split(" -> ")[1] for item in p2.split("\n")}
tn_step_cache = {}
ty_step_cache = {}
ty_elem_count = {}

for a in all_bases:
    for b in all_bases:
        tn_step_cache[a + b] = cache_steps([a, b], 10)

for a in all_bases:
    for b in all_bases:
        print(a + b)
        ty_step_cache[a + b] = []

        for i in range(len(tn_step_cache[a + b]) - 1):
            ty_step_cache[a + b].append(tn_step_cache[a + b][i])
            ty_step_cache[a + b].extend(tn_step_cache["".join(tn_step_cache[a + b][i: i + 2])])

        ty_step_cache[a + b].append(tn_step_cache[a + b][-1])
        ty_elem_count[a + b] = get_count(ty_step_cache[a + b])


new_chain = []

for i in range(len(chain) - 1):
    new_chain.append(chain[i])
    new_chain.extend(ty_step_cache["".join(chain[i: i + 2])])

new_chain.append(chain[-1])
count = {k: 0 for k in all_bases}

print(len(new_chain))
for i in range(len(new_chain) - 1):
    c_dict = ty_elem_count["".join(new_chain[i: i + 2])]

    for k, v in c_dict.items():
        count[k] += v


print(count[max(count.keys(), key=lambda x: count[x])] - count[min(count.keys(), key=lambda x: count[x])])
