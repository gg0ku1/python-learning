# E
# ED
# EDC
# EDCB
# EDCBA

def pat18(n):
    
    for row in range(1,n+1):
        for column in range(1,row+1):
            print(chr(ord('A') + (n - column )), end="")
        print()

pat18(5)