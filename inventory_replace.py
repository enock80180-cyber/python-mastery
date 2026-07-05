# Project #69: Item Replacement System

# 1. Start with our standard inventory
inventory = ["🪵 Wooden Stick", "🛡️ Sheild", "🧪 Portion"]

print("🎒 Old Inventory:")
print(inventory)

print("\n✨ You found a ⚔️ Steel Sword! Swapping it out for the stick.... ")

# Replace the item at index 0 (the wooden stick) with the new sword
inventory[0] = "⚔️ Steel Sword"

# 3. Print the updated inventory
print("\n🎒 Updated Inventory")
print(inventory)
