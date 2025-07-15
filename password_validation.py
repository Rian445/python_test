password = input("Enter your password: ")

if len(password) < 8:
    print("Password must be at least 8 characters long")
elif password != password.strip():
    print("Password should not start or end with spaces")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one number")
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter")
else:
    print("Password is valid!")
