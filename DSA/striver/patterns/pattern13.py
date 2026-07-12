# 1
# 23
# 456
# 78910
# 1112131415

def pat13(n):
    number = 1
    for row in range(1,n+1):
        for column in range(1,row+1):
            print(number, end="")
            number +=1
        print()

pat13(5)
