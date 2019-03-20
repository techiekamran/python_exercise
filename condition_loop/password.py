# Write a Python program to check the validity of a password (input from users).

# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

# Input
# W3r@100a
# Output
# Valid password


import re
x = True
while x:
    p = input("Enter the password ")
    
    if (len(p)<6 or len(p)>16):
        break
    elif not re.search('[a-z]',p):
        break
    elif not re.search('[A-Z]',p):
        break
    elif not re.search('[1-9]',p):
        break
    elif not re.search('[@#$]',p):
        break
    elif  re.search("\s",p):
        break
    else:
        print("Valid password")
        x = False
        break
    
    
if x:
    print("Not valid password")


