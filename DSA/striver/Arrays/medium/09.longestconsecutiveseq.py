# #brute force

# arr = [100, 4, 200, 1, 3, 2]
# n = len(arr)
# for i in range(n):
#     x = arr[i]
#     count = 1
#     while x + 1 in arr:
#         x += 1
#         count += 1

# print(count)

#better

arr = [100, 4, 200, 1, 3, 2]

arr = sorted(arr) 

longest = 1

lastsmaller = float("-inf")

countcurr = 0

for i in range(len(arr)):

    if arr[i] == lastsmaller:
        continue


    elif arr[i] - 1 == lastsmaller:
        countcurr += 1
        lastsmaller = arr[i]

    elif arr[i] != lastsmaller:
        countcurr = 1
        lastsmaller = arr[i]

    longest = max(longest,countcurr)

