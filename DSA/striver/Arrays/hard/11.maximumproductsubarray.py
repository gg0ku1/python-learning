nums = [2, 3, -2, 4]

max_product = float('-inf')

for i in range(len(nums)):
    product = 1

    for j in range(i, len(nums)):
        product = product * nums[j]
        max_product = max(max_product, product)

print(max_product)

#optimal 