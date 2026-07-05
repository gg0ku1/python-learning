# 12345
# 1234
# 123
# 12
# 1

def pat6(n):
    for row in range(n,0,-1):
        for col in range(row):
            print(col + 1, end = "")
        print()

pat6(5)