#swap left and right

arr = [1, 2, 3, 4, 5]

def rev(left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    rev(left+1, right-1)

n = len(arr)

rev(0, n-1)
print(arr)
