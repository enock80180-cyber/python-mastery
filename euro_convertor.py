usd_wallet = 50

# Using the forward slash '/' instead of the star symbol !
euro_wallet = usd_wallet / 1.087

print("You have Euros:")
print(euro_wallet)

if euro_wallet >= 20.0:
    print("Pack your bags, you are heading to Amsterdam!")
elif euro_wallet > 0:
    print("Not enough for the train, grab a bike instead.")
else:
    print("Your wallet is empty!")
