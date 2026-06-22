import json

contacts = []

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)

except FileNotFoundError:
    contacts = []

def add_contact():
    print ("enter contact details ")
    contact_name = input("enter name: ")
    phone_number = int(input("enter number: "))
    contact_email = input("enter email: ")

    new_contact = {"contact name":contact_name,
                   "contact number":phone_number,
                   "contact email":contact_email}
    
    contacts.append(new_contact)
    print("contact added successfully")
    save_contact()

def save_contact():
    with open("contacts.json","w") as file:
        json.dump(contacts, file)


def view_contact():
    if contacts:
        count = 1
        for contact in contacts:
            print(f"{count}. {contact["contact name"]}|{contact["contact number"]}|{contact["contact email"]} ")
            count+=1
    else:
        print("no contacts added")

def delete_contact():
    try:
        delete = int(input("enter contact to delete: "))
        if 0<delete<=len(contacts):
            del contacts[delete-1]
            print("contact deleted successfully")
        else:
            print("invalid entry")
    except(ValueError):
        print("please enter valid number")

    save_contact()

def search_contact():
    search = input("enter contact to search: ")
    found = False
    for contact in contacts:
       if contact["contact name"] == search:
           print(f'your contact is: {contact["contact name"]}|{contact["contact number"]}|{contact["contact email"]} ')
           found = True

    if found == False:
        print("Contact not found")      


while True:
    print("*************CONTACT BOOK**************")

    print("Enter choice")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contact()

    elif choice == "3":
        search_contact() 

    elif choice == "4":
        delete_contact()
    
    elif choice == "5":
        print("exiting app")
        break

    else:
        print("invalid choice")




    
