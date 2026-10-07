#brute force

arr = [2, 2, 1, 1, 1, 2, 2]

n = len(arr)

for i in range(n):
    count = 0
    for j in range(n):
        if arr[j] == arr[i]:
            count+=1

    if count > n/2:
        print(arr[i])
        break

#better - hashing

arr = [2, 2, 1, 1, 1, 2, 2]

n = len(arr)

freq = {}

for i in range(n):
    if arr[i] in freq:
        freq[arr[i]] +=1

    else:
        freq[arr[i]]= 1

for i in freq:
    if freq[i] > n/2:
        print(i)

#optimal - moores voting alg

arr = [2, 2, 1, 1, 1, 2, 2]

candidate = None
count = 0

for num in arr:
    if count == 0:
        candidate = num
        count += 1

    elif num == candidate:
        count += 1

    elif num != candidate:
        count -= 1

count = 0

for num in arr:
    if num == candidate:
        count += 1

if count > len(arr) / 2:
    print(candidate)
else:
    print("No majority element")