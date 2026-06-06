tasks = []

    #v1 complete


#for v2 we use functions
#replace all 4 features with function blocks

#for v3 we add file handling
#save tasks to file and retrieve from file

def add_task():
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")


def view_task():
        count = 1
        if tasks:
            for task in tasks:
                print(count,task)
                count += 1
        else:
            print("no tasks found")

def delete_task():
        delete = int(input("Enter task to delete:")) 
        if delete > 0 and delete <= len(tasks):
            tasks.pop(delete - 1)
            print("Task deleted successfully!")
        else:
            print("invalid")

while True:
    print("1) Add a task")
    print("2) View Tasks")
    print("3) Delete task")
    print("4) Exit")

    choice = input("Enter your choice: ")




    if choice == '1':   
         add_task()

    elif choice == "2":
        view_task()

    elif choice == '3':
        delete_task()

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid Choice")




