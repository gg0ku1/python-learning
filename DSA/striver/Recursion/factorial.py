def recur(i):
    if i == 0:
        return 0

    return i * recur(i - 1)


n = int(input())
print(recur(n))