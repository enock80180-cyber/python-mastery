# Project #62: Club Access_control
import operator

def check_access(has_invite, is_member):
    # IF either condition is True, let them in! 
    if has_invite or is_member:
       return"✨ Access Granted. Welcome to the Club!"
    else:
       return"❌ Access Denied. Sorry ,you need an invite or a membership."

print("🛡️ Security System Active\n")

# Test 1: No invite, but they ARE a member
guest_1 = check_access(False, True)

# Test 2: No invite AND not a member 
guest_2 = check_access(False, True)

print(f"Guest 1: {guest_1}")
print(f"Guest 2: {guest_2}")
