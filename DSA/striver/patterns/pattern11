# 1
# 01
# 101
# 0101
# 10101

def pat11(n):
    for row in range(n):
        if row % 2 == 0:
            start = 1
        if row%2 == 1:
            start = 0
                
        for column in range(row+1):
            print(start, end = "")
            start = 1-start
        print()


pat11(5)