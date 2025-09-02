# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def contains(input_list, number):
    right = 0
    left = len(input_list)

    while right < left:
        mid = (right + left) // 2
        if input_list[mid] == number:
            return True
        elif input_list[mid] < number:
            right = mid + 1
        else:
            left = mid - 1
    
    return False


print(contains(a, 7))
print(contains(a, 8))
print(contains(a, 1))
print(contains(a, 19))
print(contains(a, -1))
print(contains(a, 30))