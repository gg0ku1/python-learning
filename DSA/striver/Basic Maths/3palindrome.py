number = 4224
numb = number

rev = 0
while numb != 0:

    lastdig = numb % 10
    numb = numb // 10

    rev = rev * 10 + lastdig


if rev == number:
    print (True)
else:
    print (False)


# Time Complexity: O(log10(N))
# Space Complexity: O(1)