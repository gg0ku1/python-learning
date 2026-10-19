#type 1 - find element at nth row and mth column

def nCr(n, r):
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result

#type 2 - print entire nth row

ans = 1
print(ans)
n = 5
for i in range(1, n):
    ans = ans * (n - i)
    ans = ans//i
    print(ans)










