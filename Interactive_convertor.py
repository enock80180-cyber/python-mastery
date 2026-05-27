# A static test wallet that works on EVERY system flawlessly
usd_wallet = 75

print("Reading your wallet...")
print("You have USD: $" + str(usd_wallet))

# Convert to Euros using our reliable forward-slash
euro_wallet = usd_wallet / 1.087

print("Converting to Euros...")
print("You have Euros: €" + str(round(euro_wallet, 2)))

# The Decision Engine
if euro_wallet >= 20.0:
    print("Pack your bags, you are heading to Amsterdam!")
elif euro_wallet > 0:
    print("Not enough for the train, grab a bike instead.")
else:
    print("Your wallet is empty!")
