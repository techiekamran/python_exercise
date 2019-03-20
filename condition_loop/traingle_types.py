# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

def triangle(l1,l2,l3):
    if l1 == l2 == l3:
        print("equiteral triangle")
    elif l1 !=l2 !=l3 :
        print("scalene")
    else:
        print("isoscalene")
        
        

a  = int(input("Enter 1st"))
b  = int(input("Enter 2nd"))
c  = int(input("Enter 3rd"))
triangle(a,b,c)