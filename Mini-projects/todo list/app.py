tasks = []

while True:
    print("1. Add a task")
    print("2. View Tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':   
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        count = 1
        for task in tasks:
            print(count,task)
            count += 1
    
    elif choice == '3':
        delete = int(input("Enter task to delete:")) 
        tasks.pop(delete - 1)   


    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid Choice")