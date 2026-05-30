tasks = []

while True:
    print("1. Add a task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':   
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        for task in tasks:
            print(task)

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid Choice")