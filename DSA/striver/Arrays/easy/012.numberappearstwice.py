#brute force

arr = [4, 1, 2, 1, 2]

for i in range(len(arr)):
    counter = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            counter += 1

        
    if counter == 1:
        print(arr[i])