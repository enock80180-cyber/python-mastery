# 1. Attendee status
has_paid_ticket = False      # They forgot to buy a ticket!
is_guest_speaker = True      # But wait, they are speaking at the event

print("Guest walks up to the conference door....")

# 2. The 'or' check: only ONE Side needs to be True to pass
if has_paid_ticket == True or is_guest_speaker == True:
    print("--- WELCOME IN: Access granted! ---")
else:
    print("--- ACCESS DENIED: Ticket or speaker pass required. ---")
