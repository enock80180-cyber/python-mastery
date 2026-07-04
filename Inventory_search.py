# Project #66: Inventory Search System 

# 1. Setup the player's current bag
inventory = ["⚔️ Sword", "🛡️ Shield", "🔑 Boss Key", "🧪 Portion"]

print("🎒 Checking backpack content...")
print(inventory)

# 2.Define the item needed to open the dungeon gate
required_item = "🔑 Boss Key"

print("\n🚧 You approach the locked Dragon Dungeon Gate...")
print("Checking for: " + str(required_item))

# 3. Use 'in to check if the item is inside the list'
if required_item in inventory:
    print("🔓 Gate Unlocked!The " + str(required_item) + "fits peerfectly.")
else:
    print("🔒 Gate locked! You do not have the " + str(required_item) + "yet.")
