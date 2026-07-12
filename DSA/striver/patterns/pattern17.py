
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

def pat17(n):
    for row in range(n):
        for col in range(n - row - 1):
            print(" ", end = "")
        for col in range(row+ 1):
            print(chr(65 + col),end = "" )

        for col in range(row - 1, -1, -1):
            print(chr(65 + col),end = "" )

        print()

pat17(5)