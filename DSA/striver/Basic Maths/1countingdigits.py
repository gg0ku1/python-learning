import math

#brute force

numb = 12345

counter = 0 
while numb != 0:
    counter += 1
    numb = numb // 10

print(counter)



#optimal method (log)

numb = 52809

count = int(math.log10(numb)) + 1 

print(count)








# Time Complexity

# How many times does the loop run?
# For 12345, it runs 5 times.
# For 987654321, it runs 9 times.
# So it runs once per digit.
# If the number has d digits:
# Time: O(d)

# You'll often see this written as:
# O(log₁₀ N)


# Optimal (Logarithm)
# Time Complexity: O(1)
# Space Complexity: O(1)