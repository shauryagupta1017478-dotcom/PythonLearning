contact = {}

def add_contact():
    # Count existing contacts
    total_contact = len(contact)

    # Continue until there are 10 contacts
    while total_contact < 10:
        try:
            name = input("Enter contact name you want to add: ").strip()
            number = input("Enter 10-digit number you want to add: ").strip()

            if not number.isdigit():
                print("Phone number must be numeric.")
                continue
            elif len(number) != 10:
                print("Phone number must be of 10 digits.")
                continue
            elif name in contact:
                print("This contact already exists.")
                continue
            else:
                contact[name] = int(number)
                total_contact += 1
                print(f"Contact {name} added. Total contacts: {total_contact}")
        except Exception as e:
            print("Error:", e)

def display_contacts():
    print("\nFinal contact list:")
    if not contact:
        print("No contacts to show.")
    else:
        for name, number in contact.items():
            print(f"{name} : {number}")

def main():
    while True:
        print("\nEnter your choice, what do you want to do?")
        print("1. Add contact")
        print("2. Display contacts")
        print("3. Exit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            print("Exiting contact manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
print("Welcome to your contacts!")
main()
