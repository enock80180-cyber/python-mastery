# Project #45: The manifest Scanner

# 1. Here is our list of incoming frieght
manifest = ["Pallet Jack", "Safety Cones", "Bubble Wrap", "Forklift Battery"]

# 2. The loop grabs each item from the list, one by one 
for equipment in manifest:
    print(f"[UNPACKING] Recieved: {equipment}")

print("--- MANIFEST COMPLETE: All items added to inventory!---")
