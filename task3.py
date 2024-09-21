import json
import os

# Function to load contacts from a file
def load_contacts(filename="contacts.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {}

# Function to save contacts to a file
def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if name in contacts:
        print("Contact with this name already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added successfully!")

# Function to view all contacts
def view_contacts(contacts):
    if contacts:
        print("\nContact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
        print()
    else:
        print("\nNo contacts available.\n")

# Function to edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name in contacts:
        print(f"Editing contact '{name}'")
        phone = input("Enter new phone number (leave blank to keep current): ").strip()
        email = input("Enter new email address (leave blank to keep current): ").strip()

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email

        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

# Main program loop
def contact_manager():
    contacts = load_contacts()

    while True:
        print("\nContact Manager Menu:")
        print("1. Add new contact")
        print("2. View all contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
            save_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    contact_manager()
