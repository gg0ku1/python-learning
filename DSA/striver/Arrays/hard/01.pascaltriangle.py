#type 1 - find element at nth row and mth column

def nCr(n, r):
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result



