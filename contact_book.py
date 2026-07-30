CONTACT_FILE = "contacts.txt"


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")

    with open(CONTACT_FILE, "a") as file:
        file.write(f"{name},{phone}\n")

    print("✅ Contact Added Successfully!\n")


def view_contacts():
    try:
        with open(CONTACT_FILE, "r") as file:
            contacts = file.readlines()

            if not contacts:
                print("No contacts found.\n")
                return

            print("\n------ Contacts ------")
            for contact in contacts:
                name, phone = contact.strip().split(",")
                print(f"Name : {name}")
                print(f"Phone: {phone}")
                print("----------------------")

    except FileNotFoundError:
        print("No contacts found.\n")


def search_contact():
    keyword = input("Enter Name: ")

    try:
        with open(CONTACT_FILE, "r") as file:
            found = False

            for contact in file:
                name, phone = contact.strip().split(",")

                if keyword.lower() == name.lower():
                    print(f"\nFound!")
                    print(f"Name : {name}")
                    print(f"Phone: {phone}\n")
                    found = True

            if not found:
                print("Contact not found.\n")

    except FileNotFoundError:
        print("No contacts available.\n")


def delete_contact():
    keyword = input("Enter Name to Delete: ")

    try:
        with open(CONTACT_FILE, "r") as file:
            contacts = file.readlines()

        with open(CONTACT_FILE, "w") as file:
            deleted = False

            for contact in contacts:
                name, phone = contact.strip().split(",")

                if name.lower() != keyword.lower():
                    file.write(contact)
                else:
                    deleted = True

        if deleted:
            print("✅ Contact Deleted.\n")
        else:
            print("Contact not found.\n")

    except FileNotFoundError:
        print("No contacts available.\n")


while True:
    print("====== Contact Book ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice.\n")