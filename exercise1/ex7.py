# Check a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

input_str = input("Enter a string: ")

# Solution 1

reversed_str = input_str[::-1]

if input_str == reversed_str:
    print(f'"{input_str}" is a palindrome')
else:
    print(f'"{input_str}" is not a palindrome')

# Solution 2

def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

if is_palindrome(input_str):
    print(f'"{input_str}" is a palindrome')
else:
    print(f'"{input_str}" is not a palindrome')

    