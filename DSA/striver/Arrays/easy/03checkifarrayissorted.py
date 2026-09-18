arr = [1, 3, 2, 4, 5]
n = len(arr)
for i in range(1, n):
    if arr[i]< arr[i - 1]:
        print("Not sorted")
        break
