# 1      1
# 12    21
# 123  321
# 12344321


def pat12(n):
    for row in range(1, n+1):
        for column in range(row):
            print(column+1, end = "")

        for column in range(2*(n-row)):
            print(" ", end = "")

        for column in range(row):
            print(row-column, end = "")
        print()
        
pat12(4)