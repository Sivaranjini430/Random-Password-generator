#Random Password Generator
import random
import json

def generate_password():
    password_length = 8
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*-=_+?'
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    return generated_password

def save_users(existing_users):
    with open('users.json', 'w') as file:
        json.dump(existing_users, file)

def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def register_user(existing_users):
    while True:
        new_username = input("Enter your username: ")
        if new_username in existing_users:
            print("Username already exists. Please try again with a different username.")
        else:
            password = generate_password()
            print(f"Your password has been generated: {password}")
            existing_users[new_username] = password
            save_users(existing_users)
            break

def login_user(existing_users):
    while True:
        username = input("Enter your username ('show users' to display existing users, 'exit' to quit): ")

        if username == 'show users':
            print("Existing Usernames:")
            print(", ".join(existing_users.keys()))
        elif username == 'exit':
            print("Exiting program. Goodbye!")
            return False
        elif username in existing_users:
            password = input("Enter your password: ")
            if existing_users[username] == password:
                print("Successfully logged in!")
                return True
            else:
                print("Invalid password. Please try again.")
        else:
            print("Invalid username. Please try again or type 'exit' to quit.")

# Load existing users from file
existing_users = load_users()

# Ask the user whether they are a new or existing user
while True:
    user_type = input("Are you a new user or an existing user? (Type 'new' or 'existing', 'exit' to quit): ").lower()

    if user_type == 'new':
        register_user(existing_users)
    elif user_type == 'existing':
        if login_user(existing_users):
            print("Exiting program. Goodbye!")
            break
    elif user_type == 'exit':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'new', 'existing', or 'exit'.")
