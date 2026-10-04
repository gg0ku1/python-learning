#optimal

arr = [2, 3, 1, 1, 1, 1, 2]
k = 3

summ = 0
max_len = 0
hash_map = {0: -1}

for i in range(len(arr)):
    summ += arr[i]

    req = summ - k

    if req in hash_map:
        max_len = max(max_len, i - hash_map[req])

    if summ not in hash_map:
        hash_map[summ] = i

print(max_len)