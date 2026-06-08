# 1. Banned users who are NOT allowed on the server
banned_users = ["Spammer99", "Hackzero"]

# 2. Check if a normal user is safely already missing from the ban list
# Python looks and see "Malet" is missing so it says True!
is_malet_safe = "Malet" not in banned_users

print("Is Malet safe to log in ?", is_malet_safe)
