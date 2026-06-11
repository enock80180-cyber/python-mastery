 # Project #46: The Quality Control Belt

# A list of package statuses on the conveyor belt
conveyor_belt = ["Passed", "Passed", "Damaged","Passed","Damaged"]

box_number = 1

for status in conveyor_belt:
    if status == "Damaged":
       print(f"⚠️ BOX #{box_number}: CRITICAL! Item is DAMAGED. Pull it off the line!")
    else:
       print(f"✅ BOX #{box_number}: LOOKS GOOD. Moving to shipping.")

       # Increase the box number by 1 for the next loop round
       box_number = box_number + 1

print("--- INSPECTION COMPLETE: Conveyor belt cleared!---")
