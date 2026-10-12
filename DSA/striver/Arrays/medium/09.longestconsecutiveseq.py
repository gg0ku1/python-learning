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


#optimal

arr = [100, 4, 200, 1, 3, 2]

longest = 1

setnums = set(arr)

for i in setnums:
    if i - 1 in setnums:
        continue

    if i - 1 not in setnums:
        count = 1
        x = i

        while x + 1 in setnums:
            x += 1
            count += 1

        longest = max(longest, count)


