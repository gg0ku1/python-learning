numb = 12345

rev = 0
while numb != 0:

    temp = numb % 10
    numb = numb // 10

    rev = rev * 10 + temp


print(rev)

# Time Complexity: O(log10(N))
# Space Complexity: O(1)