# Project #72: Inventory Item Counter System

# 1. Setup a backpack with duplicate items
inventory = ["🧪 Portion", "⚔️ Sword", "🧪 Portion", "🛡️ Sheild", "🧪 Portion"]

print("🎒 Current Bagpack:")
print(inventory)

# 2. Use .count() to find out how many portions the player has 
portion_count = inventory.count("🧪 Portion")

print("\n🔎 Checking health supplies....")
print("🧪Total Portions found: " + str(portion_count))
