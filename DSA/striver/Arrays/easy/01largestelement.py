#brute force

arr = [5, 3, 8, 1, 4]

arr = sorted(arr)

print(f"sorted arr = {arr}")

print(f"largest = {arr[len(arr)-1]}")

#optimal

arr = [5, 3, 8, 1, 4]

largest = arr[0]

for x in arr:
    if x > largest:
        largest = x

print(largest)