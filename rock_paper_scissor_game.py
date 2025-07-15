import random
print("Welcome to the Rock Paper Scissor Game\n")
user_input = input(
    "Enter your choice Rock (R), Paper (P), or Scissors (S)): ").upper()
while user_input not in ["R", "P", "S"]:

    user_input = input(
        "Invalid choice. Please enter R, P, or S : ").upper()

compuer_choice = random.choice(["R", "P", "S"])
print(f"Computer chose: {compuer_choice}")
if user_input == compuer_choice:
    print("It's a tie!")
elif (user_input == "R" and compuer_choice == "S") or \
     (user_input == "P" and compuer_choice == "R") or \
     (user_input == "S" and compuer_choice == "P"):
    print("You win!")
else:
    print("You lose!")
print("Thank you for playing!")
