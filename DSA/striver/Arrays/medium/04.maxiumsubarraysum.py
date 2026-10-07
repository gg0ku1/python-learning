#brute force

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxi = float("-inf")
n = len(arr)
for i in range(n):
    for j in range(i,n):
        ssum = 0
        for k in range(i,j+1):
            ssum += arr[k]

        maxi = max(maxi, ssum)

print(maxi)

#better

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxi = float("-inf")
n = len(arr)
for i in range(n):
    ssum = 0
    for j in range(i,n):
        
        ssum += arr[j]

        maxi = max(maxi, ssum)

print(maxi)

#optimal - kadanes algorithm

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
ssum = 0
maxi = float("-inf")
ansstart = -1
ansend = -1

for i in range(n):
    if ssum == 0:
        start = i
    ssum += arr[i]

    if ssum > maxi:
        maxi = ssum
        ansstart = start
        ansend = i

    if ssum < 0:
        ssum = 0

print(arr[ansstart:ansend+1])
print(maxi)
