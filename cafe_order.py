# Note 1: Setting up the price of a delicious Dutch snack (Bitterballen!)
snack_price = 6.50

# Note 2: Choosing how many portions we want to order
order_quantity = 3

print("Welcome to Amsterdam! Placing your order...")

# The Math Machine: We use the plus sign three times so it works perfectly on an ipad
total_cost = snack_price + snack_price + snack_price

# Printing the final Bill
print("total for " + str(order_quantity) + "portions: €" + str(total_cost)) 

# The Decision Engine 
if total_cost > 20.0:
    print("Wow,that is a huge snack party! You get a free drink.")
else:
    print("Order placed sucessfully. Enjoy your Bitterballen!")
