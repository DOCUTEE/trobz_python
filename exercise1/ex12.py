# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, input is:
#   My name is Bond
# The output is:
#   Bond is name My


def reverse_words(input_string):
    words = input_string.split()
    words.reverse()
    return ' '.join(words)

input_string = input("Enter a long string: ")

print(reverse_words(input_string))