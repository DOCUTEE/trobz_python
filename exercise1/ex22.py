# Given an input string, count occurrences of all characters within a string
# count("pynativepynvepynative") = {'p': 3, 'y': 3, 'n': 3, 'a': 2, 't': 2, 'i': 2, 'v': 3, 'e': 3}

input_str = "pynativepynvepynative"

count_dict = {}

for ch in input_str:
    if ch in count_dict:
        count_dict[ch] += 1
    else:
        count_dict[ch] = 1

print(count_dict)