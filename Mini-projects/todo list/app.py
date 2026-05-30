tasks = []

while True:
    print("1. Add a task")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':   
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == '2':
        print("Exiting the program. Goodbye!")
        break
