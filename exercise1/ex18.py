# Given a dictionary get all values from the dictionary and add it in a list but don’t add duplicates
# speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
# Expected Outcome: [47, 52, 44, 53, 54]

speed ={
    'jan':47, 
    'feb':52, 
    'march':47, 
    'April':44, 
    'May':52, 
    'June':53, 
    'july':54, 
    'Aug':44, 
    'Sept':54
}

values = speed.values()

values = list(dict.fromkeys(values))

print(values)