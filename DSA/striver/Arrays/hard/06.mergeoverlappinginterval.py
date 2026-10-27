intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

intervals.sort()

ans = []

for interval in intervals:
    if not ans:
        ans.append(interval)

    elif interval[0] <= ans[-1][1]:
        ans[-1][1] = max(ans[-1][1], interval[1])

    else:
        ans.append(interval)

print(ans)



