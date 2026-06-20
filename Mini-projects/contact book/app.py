contacts = []


while True:
    print("*************CONTACT BOOK**************")

    print("Enter choice")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    break



def add_contact():
    print ("enter contact details: ")
    contact_name = input("enter name")
    phone_number = int(input("enter name"))
    contact_email = input("enter name")

    new_contact = {"contact name":contact_name,
                   "contact number":phone_number,
                   "contact email":contact_email}
    
    contacts.append(new_contact)
    print("contact added successfully")

def view_contact():
    if contacts:
        count = 10
        for contact in contacts:
            print(f"{count}. {contact["contact name"]}|{contact["contact number"]}|{contact["contact email"]} ")
            count+=1
    else:
        print("no contacts added")

def delete_contact():
    delete = int(input("enter contact to delete"))
    if 0<delete<=len(contacts):
        del contacts[delete-1]
        print("contact deleted successfully")
    else:
        print("invalid entry")
