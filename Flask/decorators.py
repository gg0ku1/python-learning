# def hello():
#     print("Hello")


def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper

# hello = decorator(hello)

# hello()


@decorator
def hello():
    print("Hello")

hello()