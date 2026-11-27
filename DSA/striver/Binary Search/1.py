#binary search
arr = [1, 3, 5, 7, 9, 11, 13]
target = 9

low = 0 

high = len(arr)-1

mid = (low + high) // 2 

while low <= high:
    if arr[mid] == target:
        print(target)

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

