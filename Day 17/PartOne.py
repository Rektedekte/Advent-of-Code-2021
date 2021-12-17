def get_value(data, o=0):
    if len(data) - 11 < o:
        return 0, len(data)

    version_id = int(data[o + 0: o + 3], 2)
    type_id = int(data[o + 3: o + 6], 2)

    if type_id == 4:
        i = o + 6

        while data[i] == "1":
            i += 5

        i += 5

        return version_id, i

    length_id = int(data[o + 6])

    if length_id == 0:
        sub_length = int(data[o + 7: o + 22], 2)
        n_i = o + 22
        t_sum = version_id

        while n_i < o + 22 + sub_length:
            sub_sum, n_i = get_value(data, n_i)
            t_sum += sub_sum

        return t_sum, n_i

    else:
        sub_length = int(data[o + 7: o + 18], 2)
        n_i = o + 18
        t_sum = version_id

        for _ in range(sub_length):
            sub_sum, n_i = get_value(data, n_i)
            t_sum += sub_sum

        return t_sum, n_i


def hex_to_bin(data):
    n = int(data, 16)
    b = bin(n)

    return b[2:]


with open("input.txt", "r") as f:
    con = f.read()


bin_num = hex_to_bin(con)
print(get_value(bin_num)[0])
