arr = [10,5,10,15,10,5]

freq = {}

for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]] += 1
    else:
        freq[arr[i]] = 1

print(freq)

highest = 0
lowest = 0
for key,value in freq.items():
    if value > highest:
        value = highest

    if value < lowest:
        value = lowest

    print(f"highest = {key(highest)},{highest}")
    print(f"lowest = {key(lowest)},{lowest}")
        

        