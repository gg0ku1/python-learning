#brute force

arr = [1,2,3,4,5,6,7]
d = 3



n = len(arr)
temp = arr[n-d:]

for i in range(n-d-1,-1, -1):
    arr[i+d] = arr[i] 

for i in range(d):
    arr[i] = temp[i]

print(arr)

#optimal

arr = [1,2,3,4,5,6,7]
d = 3

def reverse(left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse(left+1, right-1)

n = len(arr)

reverse(0, d-1)
reverse(d, n-1)
reverse(0, n-1)

print(arr)