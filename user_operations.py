# user_operations.py

from userdata import users

def add_user(username, password):
    users.append({"username": username, "password": password})
    print(f"User '{username}' added successfully.")

def list_users():
    if not users:
        print("No users found.")
    else:
        print("Registered users:")
        for user in users:
            print(f"- {user['username']}")

def delete_user(username):
    for user in users:
        if user['username'] == username:
            users.remove(user)
            print(f"User '{username}' deleted.")
            return
    print(f"User '{username}' not found.")

def authenticate(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            print(f"Login successful for user '{username}'!")
            return True
    print("Invalid username or password.")
    return False
