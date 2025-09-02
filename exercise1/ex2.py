# Get a string from the user and display only those characters which are present at an even index
# For example str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

input_str = input()

choose_items = [element for index, element in enumerate(input_str) if index % 2 == 0]

print(",".join(choose_items))