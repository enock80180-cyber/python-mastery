Project #65: Inventory Reset System

# 1. Start with our inventory list from  project 64
inventory = ["⚔️ Sword", "🛡️ Shield", "🔑 Gold Key"]

print("🎒 Inventory before defeat:")
print(inventory)

# 2. Player loses! We clear the entire list using .clear()
inventory.clear()
print("\n💀 Player defeated! Clearing backpack...")
print(inventory)

# 3. Game restarts! Give them a basic wooden stick to start over
inventory.append("🪵 Wooden Stick")
print("\n🔄 Game restarted! New starter item added:")
print(inventory)

# 4. Count the new starting items
final_count = len(inventory)
print("\n📊 Total items in new bag:" + str(final_count))
