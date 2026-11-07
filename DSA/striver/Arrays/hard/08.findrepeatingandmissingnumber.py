#brute force

arr = [3, 1, 2, 5, 3]
n = len(arr)

repeating = -1
missing = -1

for i in range(1, n + 1):
    count = 0

    for j in range(n):
        if arr[j] == i:
            count += 1

    if count == 2:
        repeating = i
    elif count == 0:
        missing = i

print("Repeating:", repeating)
print("Missing:", missing)

#better - hashing

arr = [3, 1, 2, 5, 3]
n = len(arr)

freq = [0] * (n + 1)

for num in arr:
    freq[num] += 1

repeating = -1
missing = -1

for i in range(1, n + 1):
    if freq[i] == 2:
        repeating = i
    elif freq[i] == 0:
        missing = i

print("Repeating:", repeating)
print("Missing:", missing)

