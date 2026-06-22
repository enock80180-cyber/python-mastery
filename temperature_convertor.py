#Project #58: Temperature Converter (Math in Functions)
import operator

def convert_to_fahrenheit(celsius):
    # Apply the conversion math formula
    #operator.mul(a, b) multiplies a and b together without using the * key 
    fahrenheit = operator.mul(celsius, 1.8) + 32
    return fahrenheit

print("🌡️ Weather Station Tool Active\n")

# Test the function with room 
room_temp = convert_to_fahrenheit(20)
freezing_temp = convert_to_fahrenheit(0)

print(f"20 celcuis in Fahrenheit is: {room_temp}Fahrenheit")
print(f"0 celcuis in Fahrenheit is: {freezing_temp}Fahrenheit")
