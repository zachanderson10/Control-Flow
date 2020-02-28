

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
# been met.  If not it will run again until
# the condition, #10, is met

while x <= 10:
    print (x)
    x = x + 1





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



"""
Programmer: Zach Anderson
Date: 12.16.19
Average test scores

# Programmer: Zach Anderson
# Date: 1/20/20
# Program: Double For Loop

for i in range(3):
    print("Outer For Loop " + str(i))
    for k in range(4):
        print("\tInner For Loop " + str(k))

"""
total = 0
how_many_tests = int(input("How many test do you need to average? "))

print("")
for i in range(how_many_tests):
    score = float(input("Enter a score: "))
    total = total + score

average = total / how_many_tests

print("")

print("Average: " + str(round(average, 2)))

print("")

print("The data type of the variable average is..." + str(type(average)))



"""
Programmer: Zach Anderson
Date: 1/23/20
Program: While Loop nested inside of a For Loop

"""

print("\n******************\n")


for i in range(4):
    print("For loop: " + str(i))
    x = i
    while x >= 0:
        print("\tWhile Loop: " + str(x))
        x = x - 1
        

# Date: 2/3/20
# Programmer: Zach Anderson
# Declare Global Variables here......

# name = input("\nWhat is your name: ")
x = 15


# Create Functions Here......

# Greeting Function
def greeting():
    print("Hi there " + name + "!")
    print("Very nice to meet you " + name)
    print(x)


# Functions & Local Variable x
def printsomething():
    x = 3
    print(x)

# Functions & Parameters
def printNumber(age): #function name = printNumber with a Parameter of age
    print(age)

# Default Parameter Values
def printTwoNumbers(x, y = 71):
    print("First Parameter(Number):" + str(x))
    print("Second Parametr(Number): " + str(y))

# Print sum
def printSum(x,y):
    print(x + y)

# Print Multiple Times
def printMultipleTimes(string, times):
    for i in range(times):
        print(string)

# Call Functions Here......

print("\n****Greetings Function****\n")
greeting(x)
print("\n****Print Something Function****\n")
printsomething(x)

print(x)
print("\n****Print Number Function****\n")
# printNumber(17)
# printNumber(15)
print("\n****Print Two Numbers Function****\n")
# printTwoNumbers(23,78)
# printTwoNumbers(45)
print("\n****Print Sum Function****\n")
# printSum(36,29)
print("\n****Print Multiple Times Function****\n")
# printMultipleTimes("I love Computer Science", 13)
>>>>>>> Functions&Parameters
