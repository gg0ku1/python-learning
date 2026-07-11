# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


def pat10(n):

    for row in range(1, 2*n):

        stars = row

        if row > n:
            stars = 2*n - row

        for _ in range(stars):
            print("*", end="")

        print()

pat10(5)
