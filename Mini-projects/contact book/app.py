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
                   "phone_number":phone_number,
                   "contact_email":contact_email}
    
    contacts.append(new_contact)