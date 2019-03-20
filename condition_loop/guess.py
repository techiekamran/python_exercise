# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random
count=0
ran = random.randint(1,9)
    
while(True):
    num = int(input("Enter the any number "))
    count += 1
    if num == ran:
        print("You guess true number ",ran)
        print("You take ",count,"chance")
        break
    elif num>ran:
        print("Your no is too high")
    else:
        print("Your no is too low")
    r=input("You want to conyininue (y/n) ")
    if r== "y":
        continue
    else:
        break