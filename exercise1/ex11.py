# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Note: Write two different functions to do this - one using a loop and constructing a list, and another using sets.


a = [5,5,4,3,1,4,2,2,1]

# Solution 1: Set

def remove_duplicates(input_list):
    return list(set(input_list))

print(remove_duplicates(a))

# Solution 2: Loop
def remove_duplicates_loop(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

print(remove_duplicates_loop(a))

# Solution 3: Optimized Loop O(n log n)
def remove_duplicates_optimized(input_list):
    if (not input_list):
        return []
    input_list.sort()
    output_list = [input_list[0]]
    for item in input_list:
        if item != output_list[-1]:
            output_list.append(item)

    return output_list

print(remove_duplicates_optimized(a))