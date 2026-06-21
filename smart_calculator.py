Project #56: Smart Calculator (Multiple Parameter + Return)

# This function expects TWO inputs: num1 and num2
def add_numbers(num1, num2):
    results = num1 + num2
    return results

print("🧮 Calculator Booting Up...\n")

# Call the function with different pairs of numbers
total_1 = add_numbers(10, 5)
total_2 = add_numbers(150, 250)

print(f"First calculation (10 + 5) ={total_1}")
print(f"Second calculation (150 + 250) ={total_2}")
