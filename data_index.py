# 1. The lineup of shipping containersat the dock
cargo_dock = ["GEAR-A", "FOOD-01", "MED-CORPS", "TEXT-88", "ELEC-04"]

# 2. Use the .index() tool to find the exact slot location
target_slot = cargo_dock.index("MED-CORPS")

# 3.Print out the location results
print("=== DOCK POSITION LOCATOR ===")
print("Container MED-CORPS is located at Slot Number:", target_slot)
print("==============================")
