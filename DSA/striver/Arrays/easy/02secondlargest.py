#brute force

arr = [5, 8, 8, 1, 4]

n = len(arr)

arr = sorted(arr)

print(f"sorted arr = {arr}")

for i in range(n-1,-1,-1):
    if arr[i]<arr[n-1]:
        print(f"second largest = {arr[i]}")
        break

#better solution

arr = [5, 3, 8, 1, 4]

largest = arr[0]
second_largest = arr[0]

for x in arr:
    if x > largest:
        largest = x

for y in arr:
    if y > second_largest and y != largest:
        second_largest = y

print(second_largest)

#optimal solution

arr = [5, 3, 8, 1, 4]

largest = arr[0]
second_largest = float("-inf")

for x in arr:
    if x > largest:
        second_largest = largest
        largest = x

    elif x > second_largest and x != largest:
        second_largest = x

print(second_largest)
 