# 1. A log of customer support tickets statuses
tickets_status = ["Closed", "Pending", "Open", "Pending", "Closed", "Pending"]

# 2. Use the .count() tool to scan for a specific repeating word
Pending_counting = tickets_status.count("Pending")

# 3. Print the results clearly
print("=== CALCO TICKET AUDIT===")
print("Total Pending tickets found:", Pending_counting)
print("===========================")
