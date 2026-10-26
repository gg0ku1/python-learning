#brute force
arr = [1, 2, 3]
p = 3
count = 0

for i in range(len(arr)):
    for j in range(i, len(arr)):
        xorr = 0
        for k in range(i,j+1):
            xorr = xorr ^ arr[k]

        if xorr == p:
            count +=1


#better

arr = [1, 2, 3]
p = 3
count = 0

for i in range(len(arr)):
    xorr = 0
    for j in range(i, len(arr)):
        xorr = xorr ^ arr[j]

        if xorr == p:
            count +=1

#optimal

arr = [1, 2, 3]
k = 3

count = 0
current_xor = 0
freq = {0: 1}

for num in arr:
    current_xor = current_xor ^ num

    need = current_xor ^ k

    count += freq.get(need, 0)
    freq[current_xor] = freq.get(current_xor, 0) + 1

print (count)