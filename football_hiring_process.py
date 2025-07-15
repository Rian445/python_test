print("Welcome to the Football Selection Team Form\n")

user_name = input("What is your name?\n")
print()

# Age input with validation
while True:
    try:
        user_age = int(input("What is your age?\n"))
        break
    except ValueError:
        print("Please enter a valid number for age.\n")

print()

# Gender input with validation
user_gender = input("Male / Female?\n").strip().upper()
while user_gender not in ["MALE", "FEMALE"]:
    print("Invalid gender. Please enter either 'Male' or 'Female'.\n")
    user_gender = input("Male / Female?\n").strip().upper()

print()

# Decision logic
if 14 <= user_age <= 20 and user_gender == "MALE":
    print(f"Hey {user_name}, we are delighted to inform you that you are selected.")
elif user_age <= 13:
    print(
        f"Hey {user_name}, we are sorry to say that you are too young for us.")
elif 14 <= user_age <= 20 and user_gender == "FEMALE":
    print(f"Hey {user_name}, we are sorry to inform you that currently we are not looking for any female candidate.")
else:
    print(
        f"Hey {user_name}, we are sorry to inform you that you are too old for our selection.")
