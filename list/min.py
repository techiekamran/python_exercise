# Write a Python program to get the smallest number from a list.
# max_num_in_list([1, 2, -8, 0])
# return 2

def check_max(l):
    maximum = l[0]
    for i in l:
        if i >  maximum:
            maximum = i
    return maximum


l = [1,2,-8,0]
print(check_max(l))