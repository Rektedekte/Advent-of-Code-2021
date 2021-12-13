with open("input.txt", "r") as f:
    lines = f.read().split("\n")


it = map(lambda line: line.split("|"), lines)

table = {
    0: {"a", "b", "c", "e", "f", "g"},
    1: {"c", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    4: {"b", "c", "d", "f"},
    5: {"a", "b", "d", "f", "g"},
    6: {"a", "b", "d", "e", "f", "g"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"}
}


def parse(seg_to_wire, digit):
    translated_digit = set()

    for let in digit:
        translated_digit.add(seg_to_wire[let])

    for key, val in table.items():
        if val == translated_digit:
            return key


c = 0

for uniques, out in it:
    pot_map = {
        "a": set(),
        "b": set(),
        "c": set(),
        "d": set(),
        "e": set(),
        "f": set(),
        "g": set()
    }

    size_sorted = {
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: []
    }

    for digit in uniques.rstrip(" ").split(" "):
        size_sorted[len(digit)].append(digit)

    pot_map["c"].add(size_sorted[2][0][0])
    pot_map["c"].add(size_sorted[2][0][1])
    pot_map["f"].add(size_sorted[2][0][0])
    pot_map["f"].add(size_sorted[2][0][1])

    for let in size_sorted[3][0]:
        if let not in pot_map["c"]:
            pot_map["a"].add(let)

    for let in size_sorted[4][0]:
        if let not in pot_map["c"]:
            pot_map["b"].add(let)
            pot_map["d"].add(let)

    for digit in size_sorted[6]:
        inter = pot_map["c"].intersection(set(digit))
        if len(inter) != 2:
            pot_map["f"] = pot_map["f"].intersection(inter)
            pot_map["c"] = pot_map["c"].difference(inter)
            break

    for i, digit in enumerate(size_sorted[5]):
        inter = pot_map["c"].intersection(set(digit))
        if len(inter) == 0:
            collected = set("".join(d for j, d in enumerate(size_sorted[5]) if i != j))
            unique = set(digit).difference(collected)
            pot_map["b"] = pot_map["b"].intersection(unique)
            break

    for let in size_sorted[4][0]:
        if let not in pot_map["b"] and let not in pot_map["c"] and let not in pot_map["f"]:
            pot_map["d"].clear()
            pot_map["d"].add(let)

    six_or_nine = list(digit for digit in size_sorted[6] if pot_map["d"].intersection(set(digit)))

    if pot_map["c"].intersection(set(six_or_nine[0])):
        nine = six_or_nine[0]
        six = six_or_nine[1]
    else:
        nine = six_or_nine[1]
        six = six_or_nine[0]

    dist = set(six).difference(set(nine))
    pot_map["e"] = dist

    marked = set().union(*pot_map.values())
    pot_map["g"] = pot_map["g"].union({"a", "b", "c", "d", "e", "f", "g"}.difference(marked))

    trans_table = {}

    for key, val in pot_map.items():
        trans_table[val.pop()] = key

    res = []
    for digit in out.lstrip(" ").split(" "):
        res.append(parse(trans_table, digit))

    res = "".join(map(str, res))
    c += int(res)

print(c)
