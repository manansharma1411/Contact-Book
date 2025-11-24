import json
import os
CONTACTS_FILE = 'contacts.json'
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, 'r') as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError):
            print("⚠️ Could not load contacts file. Starting with an empty list.")
            return {}
    return {}
def save_contacts(data):
    try:
        with open(CONTACTS_FILE, 'w') as file:
            json.dump(data, file, indent=4)
        print("✅ Contacts saved successfully!")
    except IOError:
        print("❌ Error saving contacts to file!")
contacts = load_contacts()
def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name (required): ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    if name and (phone or email):
        if name in contacts:
            print(f"⚠️ Warning: Contact '{name}' already exists. Use Update (4) to modify.")
        else:
            contacts[name] = [phone, email]
            print(f"➕ Contact '{name}' added!")
    else:
        print("❌ Name is required. Contact not added.")
def view_contacts():
    if not contacts:
        print("\nℹ️ No contacts to display.")
        return
    print("\n--- Current Contact List ({}) ---".format(len(contacts)))
    for name, info in contacts.items():
        print(f"Name: {name:<20} | Phone: {info[0]:<15} | Email: {info[1]}")
    print("---------------------------------------")
def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"\n✅ Found: Name: {name} | Phone: {info[0]} | Email: {info[1]}")
    else:
        print(f"❌ Contact '{name}' not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        current_phone, current_email = contacts[name]
        print(f"Current details: Phone: {current_phone}, Email: {current_email}")
        phone = input("New Phone (leave blank to keep current): ")
        email = input("New Email (leave blank to keep current): ")
        new_phone = phone if phone else current_phone
        new_email = email if email else current_email
        contacts[name] = [new_phone, new_email]
        print(f"🔄 Contact '{name}' updated successfully!")
    else:
        print(f"❌ Contact '{name}' not found. Cannot update.")

def delete_contact():
    """Deletes a contact by name."""
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact '{name}' deleted!")
    else:
        print(f"❌ Contact '{name}' not found. Cannot delete.")
print("\n✨ Welcome to the Console Contact Manager ✨")
while True:
    print("\n")
    print("-"*40)
    print("      CONTACT MANAGER MENU")
    print("-"*40)
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact by Name")
    print("4. Update Contact Details")
    print("5. Delete Contact")
    print("6. Save & Exit")
    print("-"*40)
    ch = input("Enter your choice (1-6): ")
    if ch=="1": 
        add_contact()
    elif ch=="2": 
        view_contacts()
    elif ch=="3": 
        search_contact()
    elif ch=="4": 
        update_contact()
    elif ch=="5": 
        delete_contact()
    elif ch=="6":
        save_contacts(contacts)
        print("👋 Application exiting. Goodbye!")
        break
    else: 
        print("🛑 Invalid choice, please enter a number from 1 to 6.")