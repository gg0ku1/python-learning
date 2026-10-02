arr = [1, 1, 0, 1, 1, 1]

counter = 0
max1 = 0

for x in arr:
    if x == 1:
        counter +=1
        max1 = max(max1, counter)

    else:
        counter = 0

print(max1)