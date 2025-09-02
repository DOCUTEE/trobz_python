# Given a list of ints, return True if the first and last number of a list is the same

def same_first_last(nums):
    if len(nums) <= 1:
        return True
    return nums[0] == nums[-1]

a = [10, 20, 30, 40, 10]

print(same_first_last(a))