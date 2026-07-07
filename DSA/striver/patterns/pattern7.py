#     *
#    ***
#   *****
#  *******
# *********

def pat7(n):
    for row in range(n):
        for col in range(n - row - 1):
            print(" ", end = "")
        for col in range(2*row+ 1):
            print("*",end = "" )
        

        print()

pat7(5)