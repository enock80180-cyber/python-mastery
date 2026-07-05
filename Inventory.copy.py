Project #70: Inventory Backup System

# 1. Player's current inventory
current_inventory = ["⚔️ Steel Sword", "🛡️ Sheld", "💎 Rare Gem"]
print("🎒 Current Active Bag:")
print(current_inventory)

# 2. Create a secure backup copy before entering a boss room 
print("\n💾 Creating a save state backup.....")
backup_inventory = current_inventory.copy()

# 3. Simulate getting defeated and losing an item
current_inventory.remove("💎 Rare Gem")
print("\n💀 You were defeated and dropped your Rare Gem!")
print("🎒 Active Bag now:", current_inventory)

# 4. Restore the inventory from our backup copy 
print("\n🔄 Loading save state...Restoring items")
current_inventory = backup_inventory.copy()
print("🎒 Restored Bag:", current_inventory)
