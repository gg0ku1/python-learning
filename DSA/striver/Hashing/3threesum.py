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


#