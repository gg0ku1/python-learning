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

#type 3 - print entire pascals triangle for n

def generaterow(n):
    ans = 1
    ansrow = []
    ansrow.append(ans)

    for i in range(1, n):
        ans = ans * (n - i)
        ans = ans//i
        ansrow.append(ans)

    return ansrow

def pascaltriangle(n):
    triangle = []

    for i in range(1,n+1):
        ansrow = generaterow(i)
        triangle.append(ansrow)

    return triangle








