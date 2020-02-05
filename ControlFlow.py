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

# print(x)
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