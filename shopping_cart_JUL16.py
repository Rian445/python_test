available_items = [
    ["Apple", 30],
    ["Banana", 10],
    ["Orange", 25],
    ["Milk", 50],
    ["Bread", 40]
]

cart = []

print("Welcome to Rian’s Shop!")
print("Available Items:")

for item in available_items:
    print(item[0], "- $", item[1])

while True:
    choice = input(
        "\nEnter item name to add to cart (or 'done' to checkout): ")
    choice = choice.strip().title()

    if choice.lower() == "done":
        break

    found = False

    for item in available_items:
        if item[0] == choice:
            found = True
            if item in cart:
                print(choice, "is already in your cart.")
            else:
                cart.append(item)
                print(choice, "added to cart.")
            break

    if found == False:
        print("Item not found. Please choose from the list.")

print("\n🧾 Checkout:")
if len(cart) == 0:
    print("Your cart is empty.")
else:
    total = 0
    for item in cart:
        print("-", item[0], ": $", item[1])
        total += item[1]
    print("Total: $", total)
