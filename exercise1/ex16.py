# Given the following two sets find the intersection and remove those elements from the first set
# First Set  {65, 42, 78, 83, 23, 57, 29}
# Second Set  {67, 73, 43, 48, 83, 57, 29}


# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}

first_set = {65, 42, 78, 83, 23, 57, 29}
second_set = {67, 73, 43, 48, 83, 57, 29}

intersection = first_set & second_set
print("Intersection is ", intersection)

first_set -= intersection
print("First Set after removing common element ", first_set)