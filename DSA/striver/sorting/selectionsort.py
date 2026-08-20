min_index = 0
arr = [3, 5, 1, 2, 4]
n = len(arr)


for i in range(n):
    min_index = i

    for j in range(i, n):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)