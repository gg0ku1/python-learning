# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *



def pat20(n):
    for row in range(n):
        for col in range(row+1):
            print("*", end = "")
        for col in range(2 * (n - row - 1)):
            print(" ",end = "" )
       
        for col in range(row+1):
            print("*", end = "")
        print()

    for row in range(1,n):
        for col in range(n-row):
            print("*", end = "")

        for col in range(2*row):
            print(" ",end = "" )
       
        for col in range(n - row):
            print("*", end = "")
        print()


pat20(5)