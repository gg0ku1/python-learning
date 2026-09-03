def partition(arr, low, high):

    pivot = arr[low]
    i = low
    j = high

    while i < j:

        while arr[i] <= pivot and i <= high - 1:
            i += 1

        while arr[j] > pivot and j >= low + 1:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j

def quick_sort(arr, low, high):

    if low < high:
        pivot = partition(arr, low, high)

         
        quick_sort(arr,low,pivot )
        quick_sort(arr, pivot + 1, high)

array = [7,3,8,2,6,1,5,4]

quick_sort(array, 0,len(array)-1)
print(array)