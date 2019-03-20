# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615



n = str(input("Enter the any number"))
result = int(n) + int(n*2) + int(n*3)
print("Your result is ",result)
