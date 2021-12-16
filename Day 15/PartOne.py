def step():
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if dij_map[i][j]:
                

with open("input.txt", "r") as f:
    data = f.read()


arr = [list(map(int, line)) for line in data.split("\n")]
dij_map = [[0 for j in range(len(arr[0]))] for i in range(len(arr))]
