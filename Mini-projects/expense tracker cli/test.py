#diction = {"fruit":"apple",
 #          "fruit": "orange"}


#print(diction["fruit"])

#Expense Name: Lunch
#Amount: 250
#Category: Food


expenses = [
    {
        "expense_name": "Lunch",
        "amount": 250,
        "category": "Food"
    },
    {
        "expense_name": "Coffee",
        "amount": 120,
        "category": "Drink"
    },

        {
        "expense_name": "Uber",
        "amount": 300,
        "category": "Transport"
    }
]
'''
exp1 = input("enter expense name: ")
exp2 = int(input("enter expense amount: "))
exp3 = input("enter expense category: ")



new_expense = {
    "expense_name": exp1,
    "amount": exp2,
    "category": exp3
}

expenses.append(new_expense)
'''
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

count1 = 0
for expense in expenses:
    sum = count1 + expense["amount"]
    count1 = sum

print(f"total spending = {sum}")