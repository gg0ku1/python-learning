#brute force using set

arr = [1, 1, 2, 2, 3, 3, 4]

st = set()

for x in arr:
    st.add(x)

i = 0

for x in st:
    arr[i] = x
    i += 1

print(arr)
print(i)

# optimal approach using two pointer

arr = [1, 1, 2, 2, 3, 3, 4]
n = len(arr)
i = 0

for j in range(1, n):
    if arr[j] != arr[i]:
        arr[i + 1] = arr[j]
        i += 1

arr = arr[:i + 1]
print(arr)
print("Unique elements:", i + 1)