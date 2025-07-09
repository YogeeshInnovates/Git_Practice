# main.py

from user_operations import add_user, list_users, delete_user, authenticate
from utils import divider

def menu():
    while True:
        divider()
        print("1. Add User")
        print("2. List Users")
        print("3. Delete User")
        print("4. Authenticate User")
        print("5. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_user(username, password)
        elif choice == "2":
            list_users()
        elif choice == "3":
            username = input("Enter username to delete: ")
            delete_user(username)
        elif choice == "4":
            username = input("Enter username: ")
            password = input("Enter password: ")
            authenticate(username, password)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    menu()
