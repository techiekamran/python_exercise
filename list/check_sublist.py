# Write a Python program to check whether a list contains a sublist.
# Input
# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
# Output



def check_substring(l,s):
    sub_string = False
    if s == []:
        sub_string = True
    elif s == l:
        sub_string = True
    elif len(s) > len(l):
        sub_string = False
    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while(n<len(s)) and (l[n+i] == s[n]):
                    n += 1
                if n == len(s):
                    sub_string = True
                    return sub_string


a = [1,2,3,4,5]
b = [3,4]
print(check_substring(a,b))