# Contact Book

contacts = {}  #Dictionary to store contacts
#Function to add contact
def add_contact():
    name = input('Enter contact name: ')
    phone_no = input('Enter contact phone number: ')
    email = input('Enter contact email address: ')
    contacts[name] = {'Phone':phone_no, 'Email':email}
    print('Contact added successfully!')

#Function to search for a contact in dictionary
def search_contact():
    name = input('Enter name whose contact you want to search: ')
    if name in contacts:
        print("Name : {}".format(name))
        print("Phone: {}".format(contacts[name]['Phone']))
        print("Email: {}".format(contacts[name]['Email']))
    else:
        print("Contact not found.")

#Function to Display all contacts
def display_contacts():
    if contacts:
        print("List of contacts: ")
        for name in contacts:
            print("Name : {}".format(name))
            print("phone: {}".format(contacts[name]['Phone']))
            print("Email: {}".format(contacts[name]['Email']))
            print('------')
    else:
        print("No contacts found.")

#Function to delete contact
def delete_contact():
    name = input('Enter the name whose contact is to be deleted: ')
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print('Contact not found.')

#Function to display menu
def functions():
    print('Welcome to the Contact Book!')
    print('1. Add Contact\n'
          '2. Search Contact\n'
          '3. Display All Contacts\n'
          '4. Delete Contact\n'
          '5. Quit')

if __name__ == '__main__':
    functions()
    while True:
        choice = input('Enter your choice(1-5) : ')
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            display_contacts()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print('GoodBye!')
            break
        else:
            print('Invalid choice. Please try again.')
