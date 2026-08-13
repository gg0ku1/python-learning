#Count frequency of each element in the array

#Problem Statement: Given an array, we have found the number of occurrences of each element in the array.

#brute force 
arr = [10,5,10,15,10,5]
visited = [False, False, False, False, False, False]
for i in range(len(arr)):
    count = 1
    if visited[i]:
        continue

    for j in range(i + 1, len (arr)):
        if arr[i] == arr[j]:
            count +=1
            visited[j] = True

    print (arr[i] , count)

#Time: O(N²)


#optimal using hashing

freq = {}

for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]] += 1
    else:
        freq[arr[i]] = 1

print(freq)

# Time:
# Building dictionary → O(N)
# Printing → O(K) (K = unique elements)

# Overall: O(N)