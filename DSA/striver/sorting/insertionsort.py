arr = [5,3,4,1,2]
n = len(arr)

for i in range (1, n):
    key = arr[i]
    for j in range(i-1):
        if arr[j]>key:
            pass
#incomplete