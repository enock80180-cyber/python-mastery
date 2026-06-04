# 1. The list of active employee IDs on the network
active_users = ["ID-10", "ID-45", "ID-45", "ID-99", "ID-23", "ID-88"]

# 2. Define the target ID we are searching for
target_search = "ID-45"

# 3. Use the plain-English "in tool inside an if-statement!
if target_search in active_users:
   print("Access verified:", target_search, "is securely logged in.")
else:
    print("Alert:", target_search, "was not found on the network!")
