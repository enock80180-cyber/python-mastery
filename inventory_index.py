# Project #68: Inventory Index System

# 1. Setup a standard player inventory
inventory = ["🛡️ Sheild", "⚔️ Sword", "🧪 Portion", "🍏 Apple"]

print("🎒 Current Inventory:")
print(inventory)

# 2. Find the exact slot (index position) of the Sword
# Remember: Python starts counting list slots from 0!
sword_slot = inventory.index("⚔️ Sword")

print("\n🔎 Searching for the position of the ⚔️ sword....")
print("📍Found! The sword is located at index slow :" + str(sword_slot))
