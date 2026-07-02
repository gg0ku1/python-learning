# *
# **
# ***
# ****
# *****


def pat2(n):
    for row in range(n):
        for column in range(row + 1):
            print("*", end = "")
        print()
        
n = int(input())

pat2(n)