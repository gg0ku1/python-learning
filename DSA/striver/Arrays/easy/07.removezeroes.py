# nums = [1, 0, 2, 0, 3, 4]
# n = len(nums)
# temp = []
# for i in range(n):
#     if nums[i] != 0:
#         temp.append(nums[i])

# for i in range (len(temp)):
#     nums[i] = temp[i]

# for i in range(len(temp), n):
#     nums[i] = 0

# print(nums)

#optimal
nums = [1, 0, 2, 0, 3, 4]
n = len(nums)

i = 0

while i < n and nums[i] != 0:
    i += 1

for j in range(i+1,n):
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1

print(nums)
