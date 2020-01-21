"""
Programmer: Zach Anderson
Date: 12.16.19
Running total Part 2
"""

sum = 0
number_of_numbers = int(input("How many numbers would you like to sum? "))

print("")


for i in range(number_of_numbers):
    next = int(input("Enter a number: "))
    sum = sum + next

print ("")
print ("Sum: " + str(sum))