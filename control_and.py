# 1. User credentials
entered_correct_password = True
is_an_admin = False        # They know the password ,but they are normal user

print("Attempting to access Admin Panel....")

# 2. The Double-Key Check
# Both conditions MUST be True to pass!
if entered_correct_password == True and is_an_admin == True:
     print("--- ACCESS GRANTED: Welcome, Administrator. ---")
else:
     print("--- ACCESS DENIED: Security clearance required. ---")

print("Security check finished.")
