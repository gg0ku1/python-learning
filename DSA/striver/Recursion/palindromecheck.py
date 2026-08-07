arr = ["m", "a", "d", "a", "m"]

def palindrome(i):
    n = len(arr)

    if i >= n//2:
        return True

    if arr[i] != arr[n - i - 1]:
        return False
    return palindrome(i+1)

print(palindrome(0))
