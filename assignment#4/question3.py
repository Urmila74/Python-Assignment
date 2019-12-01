"""
Q3 : A movie theater charges different ticket prices depending on a person’s age. If a person is under the age
of 3, the ticket is free; 
if they are between 3 and 12, the ticket is $10; and if they are over age 12, the
ticket is $15. 
Write a loop in which you ask users their age, and then tell them the cost of their movie
ticket.
"""

print("Welcome to online ticket booking system\n--------------------------------\n\nWe have different prices of tickets according your age")
presons = int(input("How many person you are: "))
total_cost = 0

for c in range(1,presons+1):
    person_age = int(input("Enter your age: "))
    if person_age <= 3 and presons == 1:
        print("You are not allow")
    elif person_age <= 12 and person_age >= 3:
        print("your ticket price will be 10$: ")
        total_cost += 10
    elif person_age >= 12:
        print("your ticket price is will be 15$: ")
        total_cost+= 15
print("Tootal price: "+str(total_cost))