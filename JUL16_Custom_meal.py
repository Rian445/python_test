def build_meal(*ingredients, **options):
    print("\n🧾 Your Custom Meal")
    print("Main Ingredients:")
    for item in ingredients:
        print("- " + item)

    print("\nOptions:")
    if not options:
        print("No custom options selected.")
    else:
        for key, value in options.items():
            print(f"{key.capitalize()}: {value}")

    print("\nEnjoy your meal!")


# Example calls:
build_meal("Rice", "Chicken", "Salad", spicy="Yes",
           sauce="Garlic", drink="Lemonade")

# Unpacking tuple and dictionary
meal_items = ("Beef", "Fries", "Coleslaw")
meal_options = {"sauce": "BBQ", "extra_cheese": "Yes", "drink": "Cola"}

build_meal(*meal_items, **meal_options)
