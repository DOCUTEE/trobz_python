# Given a string input Count all lower case, upper case, digits, and special symbols
# input_str = "P@#yn26at^&i5ve"


# Total counts of chars, digits,and symbols Chars = 8 Digits = 3 Symbol = 4

input_str = "P@#yn26at^&i5ve"

count_lower = 0
count_upper = 0
count_digit = 0
count_special = 0

for ch in input_str:
    if ch.islower():
        count_lower += 1
    elif ch.isupper():
        count_upper += 1
    elif ch.isdigit():
        count_digit += 1
    else:
        count_special += 1

print("Total counts of chars, digits,and symbols Chars =", count_lower + count_upper, "Digits =", count_digit, "Symbol =", count_special)