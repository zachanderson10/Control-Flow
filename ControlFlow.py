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
# Call Functions Here......

# greeting()
# printsomething()
# print(x)
printNumber(17)
printNumber(15)
printTwoNumbers(23,78)
printTwoNumbers(45)