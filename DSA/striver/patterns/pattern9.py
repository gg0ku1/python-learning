#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

def pat9(n):
    for row in range(n):
        for col in range(n - row - 1):
            print(" ", end = "")
        for col in range(2*row+ 1):
            print("*",end = "" )
        print()
        
    for row in range(n):
        for col in range(row):
            print(" ", end = "")
        for col in range(2*n- (2*row+1)):
            print("*",end = "" )
         
        print()

pat9(5)