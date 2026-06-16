expenses= []

file = open("expenses.txt","r")
lines = file.readlines()
for line in lines:
    line = line.strip()
    parts = line.split(",")
    expense = {
        "expense_name": parts[0],
        "amount": int(parts[1]),
        "category": parts[2]
    }
    expenses.append(expense)

'''
so this is v1 , v2 done. completed basic expense tracking and then file handling.
learnt new concepts like dictionary, split(), fstrings

now before moving on, i would like to implement try and except in this project as v3

'''
file.close()

def save_expense():
    file = open("expenses.txt", "w")
    for expense in expenses:
         line = f"{expense['expense_name']},{expense['amount']},{expense['category']}"
         file.write(line + "\n")
    file.close()

def add_expense():
        exp1 = input("enter expense name: ")
        exp2 = int(input("enter expense amount: "))
        exp3 = input("enter expense category: ")



        new_expense = {
            "expense_name": exp1,
            "amount": exp2,
            "category": exp3
        }

        expenses.append(new_expense)
        save_expense()

def view_expense():
        if expenses:
                
            count = 1
            for expense in expenses:
                
                print(count,".",
                    expense["expense_name"],
                        "|",
                        expense["amount"],
                        "|",
                        expense["category"],
                        )
                count += 1
        else:
            print("no expenses tracked")

def view_total():
    total = 0
    for expense in expenses:
        total += expense["amount"]

    print(f"total spending = {total}")

def delete_expense():
     delete = int(input("enter expense to delete"))
     if 0< delete <=len(expenses):
          del expenses[delete - 1]
          print("Expense deleted.")
          save_expense()
     else:
          print("Invalid index.")
    

while True:
    print("*******************Expense Tracker************************")
    print("1) Add Expense")
    print("2) View Expense")
    print("3) Delete Expense")
    print("4) View Total Spending")
    print("5) Exit")

    choice = input("Enter your choice: ")   

    if choice == '1':   
        add_expense()

    
    elif choice == '2':     
        view_expense()
        view_total()

    elif choice == '3':     
         delete_expense()
    
    elif choice == '4':     
         view_total()

    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid Choice") 


