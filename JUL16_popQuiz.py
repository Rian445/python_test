def show_intro(name="Guest"):
    print(f"Welcome, {name}! Let's start your quiz.\n")


def ask_question(question, option1, option2, option3, correct_option):
    print("Q:", question)
    print("1.", option1)
    print("2.", option2)
    print("3.", option3)

    answer = input("Enter option number (1, 2, or 3): ")

    if answer == "1" and option1.lower() == correct_option.lower():
        return True
    elif answer == "2" and option2.lower() == correct_option.lower():
        return True
    elif answer == "3" and option3.lower() == correct_option.lower():
        return True
    else:
        return False


def show_result(score, name, topic):
    print("\n--- Quiz Completed ---")
    print("Name:", name)
    print("Topic:", topic)
    print("Score:", score)

    if score >= 2:
        print("Great job!")
    else:
        print("Better luck next time!")


# Main Program-------------------
user_name = "Rian"
quiz_topic = "General Knowledge"
score = 0

show_intro(user_name)

if ask_question("What is the capital of France?", "London", "Paris", "Berlin", "Paris"):
    score += 1

if ask_question("Which number is even?", "3", "5", "4", "4"):
    score += 1

if ask_question("Who wrote 'Hamlet'?", "Shakespeare", "Homer", "Tolstoy", "Shakespeare"):
    score += 1

show_result(score, user_name, quiz_topic)
