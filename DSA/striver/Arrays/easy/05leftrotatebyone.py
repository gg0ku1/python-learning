arr = [1,2,3,4,5]

temp = arr[0] 
n = len(arr)
for i in range(1,n):
    arr[i - 1] = arr[i] 
    i += 1

arr[n-1] = temp

print(arr)