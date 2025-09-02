# Get two int values from the user and return their multiplier result. If it is greater than 1000, then return their sum.
# Enter first number 10
# Enter second number 20
# The result is 200

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 * num2

if result > 1000:
    result = num1 + num2

print("The result is", result)