#brute force

nums = [1, 2, 1, 1, 3, 2]

n = len(nums)

arr = []
for i in range(n):
    if len(arr) == 0 or nums[i] not in arr:
        count = 0
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1

            if count > n//3:
                arr.append(nums[i])

    if len(arr) == 2:
        break

#better - hashing