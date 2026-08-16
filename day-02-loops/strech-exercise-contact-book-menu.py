"""
Exercise: Contact book menu
Student: Sabita Rajbanshi 
Day: 2

"""
# empty dictionary to story all contacts
contacts = {}

# menu for contact book
while True:
    print("Contact Book")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # 1. Add a contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }
        print(f"Contact '{name}' added successfully.")

    # 2. Search for a contact
    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Contact found")
            print("Name:", name)
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
        else:
            print(f"Contact '{name}' not found.")

    # 3. Delete a contact
    elif choice == "3":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    # 4. Display all stored contacts
    elif choice == "4":
        if not contacts:
            print("No contacts available.")
        else:
            print("All Contacts")

            for name, details in contacts.items():
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])

    # 5. Exit the loop and end the program
    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break

    # Incase of invalid choice
    else:
        print("Your choice is invalid! Please enter a number from 1 to 5.")