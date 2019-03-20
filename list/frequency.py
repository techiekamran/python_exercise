# Write a Python program to get the frequency of the elements in a list.
# input
# L = [10,10,10,20,20,30,30,30,50,50]

# outout
# {10: 4, 20: 4, 40: 2, 50: 2, 30: 1}


import collections

L = [10,10,10,20,20,30,30,30,50,50]

fre = collections.Counter(L)
print("Oiginal list: ",L)
print("List with frequency: ",fre)