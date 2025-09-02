# Given two sets, Checks if One Set is a Subset or superset of Another Set. if the subset is found delete all elements from that set
# First Set  {57, 83, 29}
# Second Set  {67, 73, 43, 48, 83, 57, 29}


# First set is a subset of the second set - True
# Second set is a subset of First set -  False


# First set is Super set of second set -  False
# Second set is Super set of First set -  True


# First Set  set()
# Second Set  {67, 73, 43, 48, 83, 57, 29}

first_set = {57, 83, 29}
second_set = {67, 73, 43, 48, 83, 57, 29}

first_is_subset = first_set.issubset(second_set)
second_is_subset = second_set.issubset(first_set)

print("First set is a subset of the second set -", first_is_subset)
print("Second set is a subset of First set - ", second_is_subset)

first_is_superset = first_set.issuperset(second_set)
second_is_superset = second_set.issuperset(first_set)

print("First set is Super set of second set -", first_is_superset)
print("Second set is Super set of First set - ", second_is_superset)

if first_is_subset:
    first_set.clear()

if second_is_subset:
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)