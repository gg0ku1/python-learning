arr = [5, 3, 4, 1, 2]


def merge(left, right):
    temp = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1

        else:
            temp.append(right[j])
            j += 1

    while i < len(left):
        temp.append(left[i])
        i += 1

    while j < len(right):
        temp.append(right[j])
        j += 1

    return temp
    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

sorted_arr = merge_sort(arr)
print(sorted_arr)