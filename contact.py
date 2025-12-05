'''contacts = {}

while True :
    print("\n You Are In Contacts")
    print("1. Create Contacts :")
    print("2. View Contacts :")
    print("3. Update Contacts :")
    print("4. Delete Contacts :")
    print("5. Search Contacts :")
    print("6. Count Contacts :")
    print("7. Exixt From Contacts :")

    choice = int(input("Enter your choice from 1 to 7 :"))

    if choice == '1':
        name = input("Enter the name you want to add in contacts")

        if name in contacts :
            print ("Already in contacts :")
        else :
            age = int(input("Enter the age of your contacts"))
            E_main = input("Enter the main i_d of your contacts")
            mobile = int(input("Enter the mobile no. of your contacts"))

            contacts[name] = {'age':int(age) , 'E_mail':E_main , 'mobile':mobile}
        print("your contacts is crreates successfully")

    elif choice == '2' :
        name = input("Enter the name you want to view detail of... :")
        if name in contacts :
            contact = contacts[name]
            print(f'\n{name}, {E_mail} , {age} and {mobile} \nare this .....')
        else:
            print("Name is not found in your contacts , If you want to add this contacts then choose 1 option  :")

    elif choice == '3' :
        name = input("Enter the name you want to update :")
        if name in contact :
            age = input("Enter the age you want to update :")
            E_mail = input("Enter the E_mail you want to update :")
            mobile = input("Enter the no. you want to update :")

            contacts[name]={'age' : int(age) , 'E_mail' : E_main , 'mobile' : mobile}
        else :
            print("Name not found in your contacts")

    elif choice == '4' :
        name = input("Enter the name you want to delete from your contacts :")

        if name in contacts :
            del contacts[name]
            print("Your contacts is deleted successfully from your contacts :")
        else:
            print("name is not found in your contacts :")
    
    elif choice == '5' :
        search_name = input("Enter the name you want to search :")
        found = False

        for name , contact in contacts.items():
            if search_name.lower() in name.lower():
                print("Fount name and age in your contacts")

                fount = True
            if not fount:
                print ("no result found")

    elif choice == '6' :
        print (f'Total contacts in your book : {len(contacts)}')

    elif choice == '7' :
        print ("Exitx :")

        break
    
    else :
        print("Invalide choice :")

        '''
    
contacts = {}

while True:
    print("\nYou Are In Contacts")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. Exit From Contacts")

    choice = input("Enter your choice from 1 to 7: ")

    if choice == '1':
        name = input("Enter the name you want to add in contacts: ")
        if name in contacts:
            print("Already in contacts.")
        else:
            age = int(input("Enter the age of your contact: "))
            e_mail = input("Enter the email ID of your contact: ")
            mobile = input("Enter the mobile number of your contact: ")
            contacts[name] = {'age': age, 'e_mail': e_mail, 'mobile': mobile}
            print("Your contact is created successfully.")

    elif choice == '2':
        name = input("Enter the name you want to view details of: ")
        if name in contacts:
            contact = contacts[name]
            print(f"\nName: {name}")
            print(f"Age: {contact['age']}")
            print(f"Email: {contact['e_mail']}")
            print(f"Mobile: {contact['mobile']}")
        else:
            print("Name not found in your contacts. To add this contact, choose option 1.")

    elif choice == '3':
        name = input("Enter the name you want to update: ")
        if name in contacts:
            age = int(input("Enter the updated age: "))
            e_mail = input("Enter the updated email: ")
            mobile = input("Enter the updated mobile number: ")
            contacts[name] = {'age': age, 'e_mail': e_mail, 'mobile': mobile}
            print("Contact updated successfully.")
        else:
            print("Name not found in your contacts.")

    elif choice == '4':
        name = input("Enter the name you want to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Name not found in your contacts.")

    elif choice == '5':
        search_name = input("Enter the name you want to search: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found Contact - Name: {name}, Age: {contact['age']}, Email: {contact['e_mail']}, Mobile: {contact['mobile']}")
                found = True
        if not found:
            print("No result found.")

    elif choice == '6':
        print(f"Total contacts in your book: {len(contacts)}")

    elif choice == '7':
        print("Exiting contacts...")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
