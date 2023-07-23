#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import getpass

def get_master_password():
    return getpass.getpass("Enter your master password: ")

def load_passwords():
    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}
    
    return passwords

def save_passwords(passwords):
    with open('passwords.json', 'w') as file:
        json.dump(passwords, file)

def add_password(passwords, master_password):
    name = input("Enter the account name: ")
    username = input("Enter the username: ")
    password = getpass.getpass("Enter the password: ")
    passwords[name] = {'username': username, 'password': password}

    save_passwords(passwords)
    print("Password added successfully!")

def view_passwords(passwords, master_password):
    if len(passwords) == 0:
        print("No passwords saved.")
        return
    
    print("Saved passwords:")
    for name, data in passwords.items():
        print(f"Account: {name}")
        print(f"Username: {data['username']}")
        print(f"Password: {data['password']}")
        print("----")

def main():
    master_password = get_master_password()
    passwords = load_passwords()

    while True:
        print("1. Add a new password")
        print("2. View saved passwords")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_password(passwords, master_password)
        elif choice == "2":
            view_passwords(passwords, master_password)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    


# In[ ]:





# In[ ]:




