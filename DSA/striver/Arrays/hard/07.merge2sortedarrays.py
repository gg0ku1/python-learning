arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]

left = len(arr1) - 1
right = 0

while left >= 0 and right < len(arr2) and arr1[left] > arr2[right]:
    arr1[left], arr2[right] = arr2[right],arr1[left]
    left -= 1
    right += 1

arr1.sort()
arr2.sort()

#GAP METHOD

arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]

m = len(arr1)
n = len(arr2)

gap = (m + n + 1) // 2

while gap > 0:
    left = 0
    right = left + gap

    while right < m + n:

        # Both pointers in arr1
        if left < m and right < m:
            if arr1[left] > arr1[right]:
                arr1[left], arr1[right] = arr1[right], arr1[left]

        # Pointers in different arrays
        elif left < m and right >= m:
            if arr1[left] > arr2[right - m]:
                arr1[left], arr2[right - m] = arr2[right - m], arr1[left]

        # Both pointers in arr2
        else:
            if arr2[left - m] > arr2[right - m]:
                arr2[left - m], arr2[right - m] = arr2[right - m], arr2[left - m]

        left += 1
        right += 1

    if gap == 1:
        gap = 0
    else:
        gap = (gap + 1) // 2

print(arr1)
print(arr2)






