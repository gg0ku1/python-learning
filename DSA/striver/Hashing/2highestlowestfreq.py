arr = [10,5,10,15,10,5]

freq = {}

for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]] += 1
    else:
        freq[arr[i]] = 1

print(freq)

highest_element, highest_freq = list(freq.items())[0]
lowest_element, lowest_freq = list(freq.items())[0]

for key,value in freq.items():
    if value > highest_freq:
        highest_freq = value
        highest_element = key

    if value < lowest_freq:
        lowest_freq = value
        lowest_element = key

print(f"highest = {highest_element},{highest_freq}")
print(f"lowest = {lowest_element},{lowest_freq}")
        

        