# 1
# 22
# 333
# 4444
# 55555

def pat3(n):
    for row in range(1 ,n):
        for column in range(1, row + 1):
            print(row , end = " ")
        print()


pat3(5)