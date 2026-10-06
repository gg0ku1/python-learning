#better solution than sorting algs

arr = [2, 0, 2, 1, 1, 0]

count0 = 0
count1 = 0
count2 = 0

for i in range(len(arr)):
    if arr[i] == 0:
        count0 += 1

    if arr[i] == 1:
        count1 += 1

    if arr[i] == 2:
        count2 += 1


for i in range(count0):
    arr[i] = 0

for i in range(count0, count0 +count1):
    arr[i] = 1

for i in range(count0 + count1, count0+count1+ count2):
    arr[i] = 2

print(arr)

#optimal - dutch national flag    

arr = [2, 0, 2, 1, 1, 0]

low = 0
mid = 0
high = len(arr) - 1

while mid <= high:
    if arr[mid] == 0:
        arr[mid], arr[low] = arr[low], arr[mid]
        mid += 1
        low += 1

    elif arr[mid] == 1:
        mid +=1

    elif arr[mid] == 2:
        arr[mid],arr[high] = arr [high], arr[mid]
        high -= 1

print(arr)
