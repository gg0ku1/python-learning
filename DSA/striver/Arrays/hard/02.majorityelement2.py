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

ls = []
freq = {}
for x in nums:
    freq[x] = freq[x] + 1

for x, count in freq.items():
    if count > n // 3:
        ls.append(x)


#optimal - extended boyer moore

candidate1 = None
candidate2 = None
count1 = 0
count2 = 0

for x in nums:
    if x == candidate1:
        count1 += 1
    elif x == candidate2:
        count2 += 1

    elif count1 == 0:
        candidate1 = x
        count1 = 1

    elif count2 == 0:
        candidate2 = x
        count2 = 1

    else:
        count1 -= 1
        count2 -= 1


n = len(nums)
result = []

count1 = 0
count2 = 0

for x in nums:
    if x == candidate1:
        count1 += 1
    elif x == candidate2:
        count2 += 1

if count1 > n // 3:
    result.append(candidate1)

if count2 > n // 3:
    result.append(candidate2)

print(result)