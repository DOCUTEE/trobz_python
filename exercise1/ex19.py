# Given 2 strings, s1, and s2 returns a new string made of the first, middle and last char each input string
# mixString("America", "Japan") = ""AJrpan"

def first_middle_last(s):
    return s[0], s[len(s)//2], s[-1]

def mix_string(s1, s2):
    f1,m1,l1 = first_middle_last(s1)
    f2,m2,l2 = first_middle_last(s2)

    return f1 + f2 + m1 + m2 + l1 + l2

print(mix_string("America", "Japan"))