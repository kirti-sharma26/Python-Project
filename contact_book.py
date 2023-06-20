import pandas as pd

CONTACTS_FILE = 'contacts.csv'

def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")

    contact_data = {'Name': [name], 'Email': [email], 'Phone Number': [phone]}
    contact_df = pd.DataFrame(contact_data)

    contact_df.to_csv(CONTACTS_FILE, mode='a', header=False, index=False)
    
    print("Contact added successfully.")

def display_contacts():
    print("\n--- Contact List ---")
    contact_df = pd.read_csv(CONTACTS_FILE)

    if contact_df.empty:
        print("No contacts found.")
    else:
        print(contact_df.to_string(index=False))
    print("***********************")
    print("Contact list displayed.")

def search_contact():
    print("\n--- Search Contact ---")
    search_term = input("Enter search term: ")

    contact_df = pd.read_csv(CONTACTS_FILE)

    matched_contacts = contact_df[contact_df['Name'].str.contains(search_term, case=False) |
                                  contact_df['Email'].str.contains(search_term, case=False) |
                                  contact_df['Phone Number'].str.contains(search_term, case=False)]

    if matched_contacts.empty:
        print("No matching contacts found.")
    else:
        print(matched_contacts.to_string(index=False))

    print("Search completed.")

def main():
    while True:
        print("\n----- Contact Book -----")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            display_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

        print()


main()
