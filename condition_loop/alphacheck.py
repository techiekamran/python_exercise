digit =0
alphabat =0
letter = input("Enter the string ")
for i in letter:
    if i.isdigit():
        digit = digit +1
    elif i.isalpha():
        alphabat = alphabat + 1
    else:
        pass
    
print("digits are " , digit)
print("alphabats are ",alphabat)