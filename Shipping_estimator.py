Project #60: Shiiping Cost Estimator ( The ultimate Combo)
import operator #👈 Loading our trusty operator toolbox

def calculate_shipping(weight, distance, is_express):
    # Base cost: 5 dollars plus (weight multiplied by 2) 
    # Replaced (weight * 2) with operator.mul(weight, 2)
    base_cost = 5 + operator.mul(weight, 2)

    # Distance cost: 1 dollar for every 10 miles
    distance_cost = distance / 10

    total = base_cost + distance_cost

    # If express is True, add a $15 rush fee
    if is_express == True:
      total = total + 15
      return f"🚀 Express Delivery Total: ${total}"
    else:
      return f"🚚 Standard Delivery Total: ${total}"

print("📦 Logistics Cost Estimator Active\n")

# Test 1: Heavy package, short distance, standard shipping 
order_1 =calculate_shipping(10, 50, False)

# Test 2: Light package, Long distance, express shipping 
order_2 = calculate_shipping(2, 300, True)

print(order_1)
print(order_2)
