# Project #44: The Running Weight Total Tracker

# 1. Start with an empty total (0 kg)
total_weight = 0

# 2. Loop through 5 items ,each weighing 10kg
for item in range(1, 6):
    total_weight = total_weight + 10
    print(f"Loaded item #{item}. Current total weight: {total_weight} kg")

print("--- ALL BOXES SCANNED: Job done! ---")
