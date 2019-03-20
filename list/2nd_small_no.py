# Write a Python program to find the second smallest number in a list.
# input
# second_smallest([1, 2, -8, -2, 0])
# output
# -2

l = [1, 2, -8, -2, 0]
l.sort()
print(l[1])