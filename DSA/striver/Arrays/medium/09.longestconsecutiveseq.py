#brute force

arr = [100, 4, 200, 1, 3, 2]
n = len(arr)
for i in range(n):
    x = arr[i]
    count = 1
    while x + 1 in arr:
        x += 1
        count += 1

print(count)

#better

