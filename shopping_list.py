# Project #63 Dynamic Shopping List Parser

def manage_cart():
    # We use square brackets[] to create a list of items
    cart = ["🍎 Apples", "🥛 Milk", "🍞 Bread"]

    print("🛒 Initial Carts Items:")
    print(cart)

    # Let's add a new dynamicall using .append()
    cart.append("☕️Coffee")

    print("\n📦 Updated Cart (Item Added):")
    print(cart)

    # Lets's count how many items are in 'box using len()
    item_count = len(cart)
    return "Total items: " + str(item_count)

print(manage_cart())
