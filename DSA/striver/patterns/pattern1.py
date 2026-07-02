# * * * *
# * * * *
# * * * *
# * * * *


def pat1(n):
    for row in range(n):
        for col in range(n):
            print("*", end = " ")
        print()

ok = int(input("enter num"))
pat1(ok)