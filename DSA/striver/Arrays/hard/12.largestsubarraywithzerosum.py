#brute

arr = [15, -2, 2, -8, 1, 7, 10, 23]

max_length = 0

for i in range(len(arr)):
    current_sum = 0

    for j in range(i, len(arr)):
        current_sum = current_sum + arr[j]

        if current_sum == 0:
            max_length = max(max_length, j - i + 1)
        

print(max_length)

#optimal

arr = [15, -2, 2, -8, 1, 7, 10, 23]

prefix_sum = 0
max_length = 0

# Store the earliest index of each prefix sum
prefix_map = {0: -1}

for i in range(len(arr)):
    prefix_sum += arr[i]

    if prefix_sum in prefix_map:
        length = i - prefix_map[prefix_sum]
        max_length = max(max_length, length)

    else:
        prefix_map[prefix_sum] = i

print(max_length)