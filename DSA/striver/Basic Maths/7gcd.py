#brute force

a = 20
b = 15
gcd = 1
for num in range(1,min(a,b)+1):
    if a % num == 0 and b % num == 0:
        gcd = num

print(gcd)

#better approach

a = 20
b = 15
for num in range(min(a,b), 0, -1):
    if a % num == 0 and b % num == 0:
        print(num)
        break

#euclidean algorithm

a = 20
b = 15
while b != 0:
    remainder = a%b
    a = b
    b = remainder

print(a)
    

# Brute Force
# Time Complexity: O(min(a, b))
# "Better"
# Time Complexity: O(min(a, b))
# Euclid:
# O(log(min(a,b)))