#brute force

arr = [3, 0, 1]

n = len(arr) + 1

for i in range(n + 1):
    if i not in arr:
        print(i)
        break


#better solution 
 
arr = [3, 0, 1]
n = len(arr)

hash_arr = [0] * (n + 1)

for x in arr:
    hash_arr[x] = 1

for i in range(n + 1):
    if hash_arr[i] == 0:
        print(i)
        break

#optimal

n = len(arr)

summ = n*(n+1)//2

s = 0
for x in arr:
    s = s+x

print(summ - s)