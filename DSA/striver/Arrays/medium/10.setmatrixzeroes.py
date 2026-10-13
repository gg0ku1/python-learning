#brute force

matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            for x in range(cols):
                if matrix[i][x] != 0:
                    matrix[i][x] = -1

            for x in range(rows):
                if matrix[x][j] != 0:
                    matrix[x][j] = -1


for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == -1:
            matrix[i][j] = 0

print(matrix)