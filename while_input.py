# Project #50: The security Gate loop

# 1. Start with the gate Locked
driver_input = ""

# 2. keep looping AS LONG AS the driver hasnt tyoed "open"
while driver_input !="open":
    print("🔒 GATE LOCKED: Security clearance required.")

    # Ask the driver for inputand save it to our variable 
    driver_input = input ("Enter gate code (or type 'open to pass'): ")

# 3. Once they type "Open", the loop breaks and this runs
print("🔒 ACCESS GRANTED: The gate is opening. Welcome to the warehouse!")
