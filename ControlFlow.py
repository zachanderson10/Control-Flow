
# Programmer: Zach Anderson
# Date: 12.16.19
# Program: Guess My Number


myNumber = 7

print("\nGuess a number between 1 & 10\n")

# Ask users to guess
guess = int(input("Enter a Guess: "))

# Keep asking users to guess my number until
# it is equal to myNumber
while guess != myNumber:
    print("\nNope, guess again: ")
    guess = int(input("Enter a Guess: "))

print("\nCongrats, you guessed my number")


"""
Programmer: Zach Anderson
Date: 12.16.19
1 Through 10
"""

# Variable that start at 1
x = 1

# While loop that will see if the condition has
#been met.  If not it will run again until
# the condition, #10, is met

while x <= 10:
    print (x)
    x = x + 1