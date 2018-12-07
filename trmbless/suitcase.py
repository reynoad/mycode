#!/usr/bin/env python3

weight = float(input("How many pounds does your suitcase weigh? "))
if weight > 50:
    print("There is a $25 charge for luggage that heavy.")
elif weight <=50:
    print("Get on the plane! No extra charge for you!")
print("Thank you for your business.")