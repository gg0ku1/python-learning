import math

#brute force approach


n = 39

for i in range(1,n+1):
    if n % i == 0:
        print(i)



# Time Complexity: O(N)
# Space Complexity: O(number of divisors)

#optimal approach

n = 36

divisors = []

for i in range(1,int(math.sqrt(n)) + 1):
    if n % i == 0:
        divisors.append(i)
        j = n//i
        if i != j:
            divisors.append(j)
                
divisors.sort()
print(divisors)

#Time: O(√N)


