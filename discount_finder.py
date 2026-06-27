# Project #61: The VIP Discount Finder
import operator

def apply_discount(bill, is_vip):
    # Check if the bill is over 100 AND they are a VIP
    if bill > 100 and is_vip:
        final_bill = bill - 20
        return f"💳 VIP DISCOUNT Applied! New Total: ${final_bill}"
    else:
        return f"🛒 No discount. Total : ${bill}"

print("💰 Store Checkout System Active\n")

# Test Case 1: Spent $150 and IS a VIP (should get the discount)
Customer_1 = apply_discount(150, True)

# Test Case 2:Spent $150 but is NOT a VIP (Should NOT get it)
Customer_2 = apply_discount(150, False)

print(Customer_1)
print(Customer_2)
