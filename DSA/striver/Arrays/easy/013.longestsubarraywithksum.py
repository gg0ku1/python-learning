# #brute force

# arr = [2, 3, 5, 1, 9]

# k = 3
# max_len = 0

# for i in range(len(arr)):
    
#     for j in range(i,len(arr)):
#         s = 0
#         for x in range(i,j+1):
#             s += arr[x]

#         if s == k:
#             max_len = max(max_len, j - i + 1)

# print(max_len)

# #better brute force


# arr = [2, 3, 5, 1, 9]
# k = 3

# max_len = 0

# for i in range(len(arr)):
#     s = 0

#     for j in range(i, len(arr)):
#         s += arr[j]

#         if s == k:
#             max_len = max(max_len, j - i + 1)

# print(max_len)

#better  - hash map
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

#optimal - for positives array

arr = [2, 3, 1, 1, 1, 1, 2]
k = 3

left = 0
right = 0
summ = 0
max_len = 0
n = len(arr)

while right < n:
    summ += arr[right]
    
    while left <= right and summ > k:
        summ -= arr[left]
        left+= 1

    if summ == k:
        max_len = max(max_len, right - left + 1)

    right += 1

    print(max_len)

    