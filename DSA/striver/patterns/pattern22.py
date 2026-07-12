def pat22(n):
    size = 2 * n - 1

    for row in range(size):
        for col in range(size):

            top = row
            left = col
            right = size - 1 - col
            bottom = size - 1 - row

            distance = min(top, left, right, bottom)

            print(n - distance, end=" ")

        print()


pat22(4)
