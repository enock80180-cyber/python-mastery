#  Project #64: Game Inventory Manager 

# 1. Start with an inventory list
inventory = ["⚔️ Sword", "🛡️ Shield", "🧪 Potion"]

print("🎒 Starting Inventory:")
print(inventory)

# 2. Add a new item you found using .append()
inventory.append("🔑 Gold key")
print("\nChest opened! Added key:")
print(inventory)

# 3. Use the potion! We remove it using .remove()
inventory.remove("🧪 Potion")
print("\nDrank the potion! Updated Inventory:")
print(inventory)

# 4. Count the remaining items using len()
final_count = len(inventory)
print("\n📊 Total items left in bag: " + str(final_count))
