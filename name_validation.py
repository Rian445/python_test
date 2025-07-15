user_name = input("Enter your name: ")
print("\n")
while not (user_name.isalpha() and len(user_name) <= 12):
    if not user_name.isalpha():
        print("Name should not contain any space or digit.\n")
    elif len(user_name) > 12:
        print("Name is too long. Please enter a name with 12 characters or less.\n")
    user_name = input("Enter your name again: ")

print(f"welcome {user_name} to the Python programming world!")
