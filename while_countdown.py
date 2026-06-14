# Project #49: The warehouse Countdown Clock

#  1. Start our ciountdown at 5 seconds
seconds_left = 5

# 2. Keep looping WHILE the seconds are greater than 0
while seconds_left > 0:
    print(f"⏳ Closing bay doors in: {seconds_left} seconds...")

    # Crucial step: decrease the countdownby 1 each time
    seconds_left = seconds_left - 1

# 3. What happens when the conditon is no longer true (hits 0)
print("🔒 SECURE: Bay doors are locked. Shift complete!")
