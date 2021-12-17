def parse_literal(data):
    bits = []

    for i in range(6, len(data), 5):
        bits.append(data[i + 1: i + 5])

    return int("".join(bits), 2)

def parse_id(data):
    version_id = int(data[0:3], 2)
    type_id = int(data[3:6], 2)

    if type_id == 4:
        return parse_literal(data)

    length_id = int(data[6])

    if length_id:
        pass
    else:
        pass
