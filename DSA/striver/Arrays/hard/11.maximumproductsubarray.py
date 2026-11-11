nums = [2, 3, -2, 4]

max_product = float('-inf')

for i in range(len(nums)):
    product = 1

    for j in range(i, len(nums)):
        product = product * nums[j]
        max_product = max(max_product, product)

print(max_product)

#optimal 

nums = [2, 3, -2, 4]

prefix = 1
suffix = 1
max_product = float('-inf')

n = len(nums)

for i in range(n):

    if prefix == 0:
        prefix = 1

    if suffix == 0:
        suffix = 1

    prefix = prefix * nums[i]
    suffix = suffix * nums[n - 1 - i]

    max_product = max(max_product, max(prefix,suffix))

print(max_product)