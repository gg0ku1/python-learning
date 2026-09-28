arr = [1, 0, 2, 0, 3, 4]
n = len(arr)
temp = []
for i in range(n):
    if arr[i] != 0:
        temp.append(arr[i])

for i in range (len(temp)):
    arr[i] = temp[i]

for i in range(len(temp), n):
    arr[i] = 0

print(arr)
