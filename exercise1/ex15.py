# Given a list, iterate it and count the occurrence of each element and create a dictionary to show the count of each element
# Original list  [11, 45, 8, 11, 23, 45, 23, 45, 89]
# Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

a = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count_dict = {
}

for item in a:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Original list ", a)
print("Printing count of each item  ", count_dict)