#brute force

arr = [100, 4, 200, 1, 3, 2]

leaders = []

for i in range(len(arr)):
    leader = True
    for j in range(i+1, len(arr)):
        if arr[j] > arr[i]:
            leader = False

    if leader == True:
        leaders.append(arr[i])

print(leaders)

#optimal

arr = [100, 4, 200, 1, 3, 2]

leaders = []

curr_lead = float("-inf")

n = len(arr)
for i in range(n-1, -1, -1):
    if arr[i] > curr_lead:
        curr_lead = arr[i]
        leaders.append(arr[i])


print(leaders)