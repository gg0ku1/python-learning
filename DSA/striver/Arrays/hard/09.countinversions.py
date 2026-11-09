#brute force

arr = [5, 3, 2, 4, 1]
n = len(arr)

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if arr[i]> arr[j]:
            count += 1

print(count)

#optimal

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    count = 0

    while left <= mid and right <= high:

        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1

        else:
            temp.append(arr[right])

            # All remaining elements in left half
            # are greater than arr[right]
            count += (mid - left + 1)

            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(len(temp)):
        arr[low + i] = temp[i]

    return count


def merge_sort(arr, low, high):
    count = 0

    if low >= high:
        return count

    mid = (low + high) // 2

    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid + 1, high)

    count += merge(arr, low, mid, high)

    return count


arr = [5, 3, 2, 4, 1]

result = merge_sort(arr, 0, len(arr) - 1)

print("Inversions:", result)
print("Sorted array:", arr)