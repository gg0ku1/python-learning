#brutw force

nums = [2,6,5,8,11]
target = 14  

for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print ([i, j])

#better

nums = [2,6,5,8,11]
target = 14  

hash_map = {}


for i in range(len(nums)):
    result = target - nums[i]

    if result in hash_map:
          print(i, hash_map[result])
          break
    else:
         hash_map[nums[i]] = i

    
     
