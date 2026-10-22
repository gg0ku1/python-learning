#brute

nums = [-1, 0, 1, 2, -1, -4]

ans = []
n = len(nums)
for i in range (n):
    for j in range (i+1, n):
        for k in range (j+1, n):
            if nums[i]+nums[j]+nums[k]== 0:
                temp = [nums[i], nums[j], nums[k]]
                temp.sort()
                if temp not in ans:
                    ans.append(temp)


#better

for i in range(n):
    seen = set()

    for j in range(i + 1, n):
        need = -(nums[i] + nums[j])

        if need in seen:
            temp = [nums[i], nums[j], need]
            temp.sort()
            if temp not in ans:
                ans.append(temp)

        seen.add(nums[j])

#optimal

nums = [-4, -1, -1, 0, 1, 2]

nums.sort()

for i in range(n):
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = n - 1


    while left < right:

        total = nums[i]+nums[left]+nums[right]

        if total == 0:
            temp = [nums[i], nums[left], nums[right]]
            ans.append(temp)
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1

            while left < right and nums[right] == nums[right + 1]:
                right -= 1


        elif total < 0:
            left += 1

        elif total > 0:
            right -= 1

        