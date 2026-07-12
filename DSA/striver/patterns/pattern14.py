# A
# AB
# ABC
# ABCD
# ABCDE

def pat13(n):
    
    for row in range(1,n+1):
        for column in range(1,row+1):
            print(chr(64 + column), end="")
        print()

pat13(5)