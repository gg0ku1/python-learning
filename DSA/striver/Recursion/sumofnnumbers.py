#parameterized recursion
def recur(i, sum):
    if i == 0:
        print(sum)
        return

    
    recur(i - 1, sum + i)


i = int(input())   


recur(i, 0)

#functional recursion

def recur(i):
    if i == 0:
        return 0

    return i + recur(i - 1)


n = int(input())
print(recur(n))