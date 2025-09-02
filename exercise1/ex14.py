# Implement a function that takes as input three variables, and returns the largest one. Do this without using the Python max() function!

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

print(largest_of_three(1, 2, 3))
print(largest_of_three(3, 2, 1))
print(largest_of_three(2, 3, 1))
print(largest_of_three(3, 4, 1))
print(largest_of_three(3, 1, 3))

