# Write a Python program to get the difference between the two lists
# Input 
# list1 = [1, 2, 3, 4]
# list2 = [1, 2]
# Output
# [3,4]

l1 = [1,2,3,4]
l2 = [1,2]
print("First method:")
print(list(set(l1)-set(l2)))



# second method

l1 = [1,2,3,4]
l2 = [1,2]
l3 = []
for i in l1:
    if i not in l2:
        l3.append(i)
        
print("second method: ",l3)