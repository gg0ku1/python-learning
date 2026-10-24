#brute

nums = [1, 0, -1, 0, -2, 2]
target = 0

ans = []
n = len(nums)
for i in range (n):
    for j in range (i+1, n):
        for k in range (j+1, n):
            for l in range(k+1,n):
                if nums[i]+nums[j]+nums[k]+nums[l]== target:
                    temp = [nums[i], nums[j], nums[k],nums[l]]
                    temp.sort()
                    if temp not in ans:
                        ans.append(temp)


#better

for i in range(n):
    for j in range(i + 1, n):
        seen = set()

        for k in range(j + 1, n):
            need = target-(nums[i] + nums[j]+ nums[k])

            if need in seen:
                temp = [nums[i], nums[j], nums[k], need]
                temp.sort()

                if temp not in ans:
                    ans.append(temp)

            seen.add(nums[k])


#optimal

nums = [-4, -1, -1, 0, 1, 2]

nums.sort()

for i in range(n):
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    for j in range(i+1, n):
        if j > i+1 and nums[j] == nums[j - 1]:
            continue
        left = j + 1
        right = n - 1


        while left < right:

            total = nums[i]+nums[j]+nums[left]+nums[right]

            if total == target:
                temp = [nums[i],nums[j], nums[left], nums[right]]
                ans.append(temp)
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1


            elif total < target:
                left += 1

            elif total > target:
                right -= 1

                