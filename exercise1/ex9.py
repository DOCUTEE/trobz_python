# Take two lists, say for example these two:
# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
# Note: Using at least one list comprehension.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Solution 1
common_elements = list(set(a) & set(b))
print(common_elements)

# Solution 2
common_elements = []
for item in a:
    if item in b and item not in common_elements:
        common_elements.append(item)    
print(common_elements)  

# Solution 3 - Using list comprehension
common_elements = list(set([item for item in a if item in b]))

print(common_elements)