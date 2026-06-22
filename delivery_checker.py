# Project #57: Delivery Checker (Functions + If/Else)

# This function checks if a package is too heavy for a standard delivery
def check_package(weight):
    if weight > 20:
       return "❌ Too heavy! Must go in a cargo truck."
    else:
       return"✅ safe! Send with regular delivery."

print("📦 Warehouse Sorting System Online\n")

# Lets test three different package weight
results_1 = check_package(19)
results_2 = check_package(40)

print(f"Package 1 (12kg): {results_1}")
print(f"Package 2 (45kg): {results_2}")
