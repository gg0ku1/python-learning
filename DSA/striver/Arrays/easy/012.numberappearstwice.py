#brute force

arr = [4, 1, 2, 1, 2]

for i in range(len(arr)):
    counter = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            counter += 1

        
    if counter == 1:
        print(arr[i])

#better approach

arr = [4, 1, 2, 1, 2]

freq = [0] * (max(arr) + 1)

for x in arr:
    freq[x] += 1

for i in range(len(freq)):
    if freq[i] == 1:
        print(i)

#optimal

arr = [4, 1, 2, 1, 2]

freq = {}

for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

for key in freq:
    if freq[key] == 1:
        print(key)
        break