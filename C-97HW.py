import random

ranNum = random.randint(1,9)
print(ranNum)

for i in range(5):
    user = int(input("Enter random number from 1-9"))
    if(user!=ranNum):
        print("Sorry! Try again.")
    if(user==ranNum):
        print("Congratulations! You got the right number")
        break