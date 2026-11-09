#brute force

arr = [5, 3, 2, 4, 1]
n = len(arr)

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if arr[i]> 2* arr[j]:
            count += 1

print(count)


#optimal

def count_pairs(arr, low, mid, high):
    count = 0
    right = mid + 1

    for left in range(low, mid + 1):

        while right <= high and arr[left] > 2 * arr[right]:
            right += 1

        count += right - (mid + 1)

    return count


def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(len(temp)):
        arr[low + i] = temp[i]


def merge_sort(arr, low, high):
    count = 0

    if low >= high:
        return count

    mid = (low + high) // 2

    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid + 1, high)

    count += count_pairs(arr, low, mid, high)

    merge(arr, low, mid, high)

    return count


arr = [5, 3, 2, 4, 1]

result = merge_sort(arr, 0, len(arr) - 1)

print("Reverse pairs:", result)
print("Sorted array:", arr)
