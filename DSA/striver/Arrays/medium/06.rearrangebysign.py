#brute force

arr = [3, 1, -2, -5, 2, -4]

pos = []
neg = []

for i in range(len(arr)):
    if arr[i]>0:
        pos.append(arr[i])

    if arr[i]<0:
        neg.append(arr[i])

for i in range(len(pos)):
    arr[2*i] = pos[i]
    arr[2*i+1] = neg[i]

print(arr)

#optimal

arr = [3, 1, -2, -5, 2, -4]
n = len(arr)
ans = [0] * n

pos = 0  
neg = 1 

for i in range(n):
    if arr[i] > 0:
        ans[pos] = arr[i] 
        pos += 2

    else:
        ans[neg] = arr[i]
        neg += 2

print(ans)