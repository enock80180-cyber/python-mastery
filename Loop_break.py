# Project #47: Emergency Stop (Using 'break')

scanned_items = ["Box 1", "Box 2", "FIRE ALARM", "Box 3", "Box 4"]

for item in scanned_items:
    if item == "FIRE ALARM":
        print("🚨 EMERGENCY: Fire alarm detected! Shutting down the belt NOW!")
        break  # This completely kills the loop immediately!
        
    print(f"[PROCESSING] {item} moved to the truck.")

print("--- SYSTEM STATE: Machine safely shut down. ---")
