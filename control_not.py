# Project #42: The maintenance check (Using "Not")
is_system_under_maintenance = False

# The "not" operator flips False into True 
# So, if maintenance is NOT happening ,let them in 
if not is_system_under_maintenance:
    print(" ---- SYSTEM ONLINE: You can login! --- ")
else:
    print("--- ACCESS DENIED: System is down for updates. ---")
