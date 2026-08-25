
arr = [3, 5, 1, 2, 4]

n = len(arr)


for i in range(n):
    didswap = False
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            didswap = True
    if didswap == False:
        break

print(arr)