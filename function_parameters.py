# Project #53: Functions with Parameters(Dynamic Inputs)

# We put 'barcode inside the ()as a placeholder variable'
def scan_box(barcode):
    print(f"📦 Scanning item code: {barcode}")
    print("⚖️ Weight logged securely.")
    print("---")

print("✅ Starting shift")

# Now,when we call the function,we give it the actual data!
scan_box("A-102")
scan_box("B-509")
scan_box("C-777")

print("🛑 Ending Shift")
