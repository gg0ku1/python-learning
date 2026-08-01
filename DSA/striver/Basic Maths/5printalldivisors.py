#brute force approach

n = 39

divisors = []
for i in range(1,n+1):
    if n % i == 0:
        divisors.append(i)

print(divisors)


# Time Complexity: O(N)
# Space Complexity: O(number of divisors)