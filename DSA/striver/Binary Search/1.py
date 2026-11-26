#binary search
arr = [1, 3, 5, 7, 9, 11, 13]
target = 9


if arr[mid] == target:
    # Found
    print(target)

elif arr[mid] < target:
    low = mid + 1

else:
    high = mid - 1