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

#better

matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

rows = len(matrix)
cols = len(matrix[0])

rowarr = [0]*rows
colarr = [0]*cols

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            rowarr[i] = 1
            colarr[j]= 1

for i in range(rows):
    for j in range(cols):
        if rowarr[i] == 1 or colarr[j] == 1:
            matrix[i][j]= 0

#optimal solution


matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

rows = len(matrix)
cols = len(matrix[0])

first_col_zero = False

for i in range(rows):
    if matrix[i][0] == 0:
        first_col_zero = True

for i in range(1,rows):
    for j in range(1,cols):
        if matrix[i][j] == 0:
            matrix[i][0] = 0
            matrix[0][j]= 0
        

for i in range(1,rows):
    for j in range(1,cols):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j]= 0

if matrix[0][0] == 0:
    for j in range(cols):
        matrix[0][j] = 0

if first_col_zero == True:
    for i in range(rows):
        matrix[i][0] = 0