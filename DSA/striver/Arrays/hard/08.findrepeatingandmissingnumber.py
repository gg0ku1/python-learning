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

#optimal- mathematical method

arr = [3, 1, 2, 5, 3]
n = len(arr)

# Expected values
expected_sum = (n * (n + 1)) // 2
expected_sq_sum = (n * (n + 1) * (2*n + 1)) // 6

# Actual values
actual_sum = 0
actual_sq_sum = 0

for num in arr:
    actual_sum = actual_sum + num
    actual_sq_sum = actual_sq_sum + num*num

# Equations
diff = actual_sum - expected_sum       # x - y
sq_diff = actual_sq_sum - expected_sq_sum  # x² - y²

val1 = diff

val2 = sq_diff//diff

x = (val1 + val2)//2
y = x - diff

repeating = x
missing = y

print("Repeating:", repeating)
print("Missing:", missing)