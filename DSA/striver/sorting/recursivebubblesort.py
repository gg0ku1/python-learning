arr = [5,3,4,1,2]

def bubble_sort(arr,n):
    if n<= 1:
        return

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    bubble_sort(arr, n - 1)


bubble_sort(arr, len(arr))
print(arr)