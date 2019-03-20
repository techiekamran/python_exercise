# Write a Python program to check a triangle is valid or not

def triangle(L1,L2,L3):
    if (L1>L2+L3) or (L2>L1+L3) or (L3>L1+L2):
        print("These sides does not form Triangle")
    elif (L1==L2+L3) or (L2==L1+L3) or (L3==L1+L2):
        print("Yes, it form degenerated Triangle")
    else:
        print("Yes, it form Triangle")
        
    
length_1 = int(input("Enter the 1st side "))
length_2 = int(input("Enter the 2nd side "))
length_3 = int(input("Enter the 3rd side "))

triangle(length_1,length_2,length_3)