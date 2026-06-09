# 1. Driver's status and balance
parking_cost = 10
user_balance = 3
has_vip_pass = True        # The driver has a pass!

print( "Driver approaches the Gate" )

# Path A: Check for standard payment
if user_balance >= parking_cost:
    print("--- GATE OPEN: Standard payment accepted! ---")

# Path B: check for a VIP pass (Only runs if Path A failed)
elif has_vip_pass == True:
    print("--- GATE OPEN: VIP Pass recognized! Welcome back! ---")

# Path C: The final fallback (only runs if BOTH Path A and B fail)
else:
    print("---- GATE CLOSED: Insufficient funds or pass missing! ----")

print("System scan complete")
