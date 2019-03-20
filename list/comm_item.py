# Write a Python program to find common items from two lists.
# input
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# output
# {'Green', 'White'}


s1 = "Red","Blue","Green","Yellow"
s2 = "Pink","Black","Green","White","Yellow"

print(set(s1) & set(s2))