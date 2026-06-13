expenses= []

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
     else:
          print("Invalid index.")
          
               
          

while True:
    print("*******************Expense Tracker************************")
    print("1) Add Expense")
    print("2) View Expense")
    print("3) Delete Expense")
    print("4) Exit")

    choice = input("Enter your choice: ")   

    if choice == '1':   
        add_expense()

    
    elif choice == '2':     
        view_expense()
        view_total()

    elif choice == '3':     
         delete_expense()

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid Choice") 


