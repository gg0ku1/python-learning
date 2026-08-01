import math

n = 2

count = 0

for i in range(1,int(math.sqrt(n)) + 1):
    if n % i == 0:
        count +=1
        j = n//i
        if i != j:
            count +=1

print(count == 2)