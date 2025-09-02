# Find all occurrences of “Viet Nam” in given string ignoring the case
# input_str = "Welcome to Viet Nam. viet nam is awesome, isn't it?"


# The ‘Viet Nam’ count is: 2

input_str = "Welcome to Viet Nam. viet nam is awesome, isn't it?"

keyword = 'Viet Nam'

count = input_str.lower().count(keyword.lower())

print(f"The ‘{keyword}’ count is:", count)