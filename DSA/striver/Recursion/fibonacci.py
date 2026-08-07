#inefficient recursion

def fib(n):
    if n >= 0:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(5))

# time complexity O(2^N) - very slow



