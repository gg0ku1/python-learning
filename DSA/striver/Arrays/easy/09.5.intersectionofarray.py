#brute force

a = [1, 2, 2, 3, 4]
b = [2, 2, 3, 5]

intersection = []
visited = [False] * len(b)

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j] and not visited[j]:
            intersection.append(a[i])
            visited[j] = True
            break

print(intersection)

#optimal

i = 0
j = 0

intersection = []

while i < len(a) and j < len(b):

    if a[i] < b[j]:
        i += 1

    elif a[i] > b[j]:
        j += 1

    elif a[i] == b [j] :
        intersection.append(a[i])
        i += 1
        j += 1

print(intersection)