# * * * *
# * * * *
# * * * *
# * * * *


def pat1(n):
    for row in range(n):
        for col in range(n):
            print("*", end = " ")
        print()

n = 4

pat1(n)