# 1
# 12
# 123
# 1234
# 12345

def pat3(n):
    for row in range(n):
        for column in range(row + 1):
            print(column + 1, end = " ")
        print()


pat3(5)