N = int(input())

list = []


for _ in range (N):
    choice = input()
    parts = choice.split()

    if parts[0] == "insert":
        i = int(parts[1])
        e = int(parts[2])
        list.insert(i, e)

    elif parts[0] == "print":
        print(list)

    elif parts[0] == "remove":
        e = int(parts[1])
        list.remove(e)

    elif parts[0] == "append":
        e = int(parts[1])
        list.append(e)

    elif parts[0] == "sort":
        list.sort()

    elif parts[0] == "pop":
        list.pop()

    elif parts[0] == "reverse":
        list.reverse()
