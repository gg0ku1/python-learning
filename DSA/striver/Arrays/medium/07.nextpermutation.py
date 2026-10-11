arr = [2,1,5,4,3,0,0]

n = len(arr)

index = -1

for i in range(n - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            index = i
            break

if index == -1:
    arr.reverse()
else:
    for i in range(n - 1, index, -1):
        if arr[i]>arr[index]:
                arr[i],arr[index] = arr[index],arr[i]
                break

    left = index + 1
    right = n - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

print(arr)