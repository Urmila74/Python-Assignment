"""
question 5
"""
import random

print("Guess the number (game)")
number = random.randint(1,30)

print("you have three chance to win this game.")
    
for x in ("abc"):
    user_number = int(input("Enter any number between 1 to 30 \n"))
    if user_number == number:
        print("you win")
        break
    if user_number >= number:
        print("numberr is less than < ",user_number)
    if user_number <= number:
        print("number is grater than > ",user_number)
else:
    print("you lose")
    print("Answer and Random ganrated number is: ",number)