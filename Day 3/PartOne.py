with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    final = [0 for i in range(12)]

    for line in lines:
        for i, bit in enumerate(line):
            if bit == "1":
                final[i] += 1

gamma_byte = "".join(map(lambda x: "1" if x >= 500 else "0", final))
epsilon_byte = "".join("0" if x == "1" else "1" for x in gamma_byte)

print(gamma_byte)
print(epsilon_byte)

gamma = int(gamma_byte, 2)
epsilon = int(epsilon_byte, 2)

print(gamma * epsilon)
