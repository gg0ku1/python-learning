#brute force

arr = [2, 3, 5, 1, 9]

k = 3
max_len = 0

for i in range(len(arr)):
    
    for j in range(i,len(arr)):
        s = 0
        for x in range(i,j+1):
            s += arr[x]

        if s == k:
            max_len = max(max_len, j - i + 1)

print(max_len)

#better brute force


arr = [2, 3, 5, 1, 9]
k = 3

max_len = 0

for i in range(len(arr)):
    s = 0

    for j in range(i, len(arr)):
        s += arr[j]

        if s == k:
            max_len = max(max_len, j - i + 1)

print(max_len)