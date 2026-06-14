#project #48: Skipping Items (Using 'continue')'

items = ["Box 1", "Empty", "Box 2", "Box 3"]

for box in items:
    if box == "EMPTY":
       print("🔄 [SYSTEM] Empty slot detected. Skipping...")
       continue  # This skips the restof THIS round and jumps to Box 2!

    print(f"📦 [PROCESSING] Sucessfully loaded {box} onto the truck.")

print("--- FINISHED: ALL valid cargo loaded!")
