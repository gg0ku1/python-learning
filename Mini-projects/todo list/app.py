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
        if len(tasks) >= 1 :
            for task in tasks:
                print(count,task)
                count += 1
        else:
            print("no tasks found")
    
    elif choice == '3':
        delete = int(input("Enter task to delete:")) 
        if delete > 0 and delete <= len(tasks):
            tasks.pop(delete - 1)
            print("Task deleted successfully!")
        else:
            print("invalid")


    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid Choice")


#v1 complete


#for v2 we use functions
#replace all 4 features with function blocks

def add_task():
    pass

def view_task():
    pass

def delete_task