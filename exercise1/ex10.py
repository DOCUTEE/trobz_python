# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

def first_and_last(input_list):
    if len(input_list) < 1:
        return []
    elif len(input_list) == 1:
        return [input_list[0]]
    elif len(input_list) > 1:
        return [input_list[0], input_list[-1]]

a = [5, 10, 15, 20, 25]

print(first_and_last(a))