import random

ranNum = random.randint(1,9)
user = input("Enter random number from 1-9")

for i in user:
    if(user!=ranNum):
        print("Sorry! Try again.")
    if(user==ranNum):
        print("Congratulations! You got the right number")
        break