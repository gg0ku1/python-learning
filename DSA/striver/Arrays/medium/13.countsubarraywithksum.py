#brute force

arr = [1, 2, 3]
p = 3
count = 0

for i in range(len(arr)):
    for j in range(i, len(arr)):
        current_sum = 0
        for k in range(i,j+1):
            current_sum = current_sum+ arr[k]

        if current_sum == p:
            count +=1


#better sokution


arr = [1, 2, 3]
p = 3
count = 0

for i in range(len(arr)):
    current_sum = 0
    for j in range(i, len(arr)):
        current_sum = current_sum+ arr[j]

        if current_sum == p:
            count +=1

#optimal solution

arr = [1, 2, 3]
k = 3
current_sum = 0
count = 0
freq = {0: 1}

for x in arr:
    current_sum += x
    need = current_sum - k

    count += freq.get(need, 0)
    freq[current_sum] = freq.get(current_sum, 0) + 1

print(count)