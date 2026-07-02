# *****
# ****
# ***
# **
# *


def pat5(n):
    for row in range(n,0, -1):
        for column in range(row):
            print("*" , end = " ")
        print()


pat5(5)