matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)

ans = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        ans[j][n-1-i] = matrix[i][j]

print(ans)

#optimal
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

for i in range(n):
    left = 0
    right = n - 1

    while left < right:
        matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
        left += 1
        right -= 1