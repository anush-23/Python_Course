"""For this challenge, you are supposed to find the sum of the digits of a two-digit number."""

x = int(input("write a two digit number to get the sum of its digits:  "))
if (10<x<99):
    print(str(x) + ' -> ' + str(x % 10 + x // 10))
else:
    print("Please enter a two digit number")



"""A repdigit is a positive number composed out of the same digit. Create a function that takes an two-digit integer and returns whether it's a repdigit or not."""

x = int(input("write a two digit number to check if it is repdigit:  "))
if (10<x<99):
    print(str(x) + ' -> ' + str(x % 10 == x // 10))
else:
    print("Please enter a two digit number")


""" Write a function that takes an integer minutes and converts it to seconds."""

def minutesToSecondsConverter(x):
    print(str(x) + ' -> ' + str(x*60))

minutesToSecondsConverter(5)
minutesToSecondsConverter(21)


"""Create a function that takes the age in years and returns the age in days."""

def yearsToDays(x):
    print(str(x) + ' -> ' + str(x*365))

yearsToDays(15)


"""Create a function that accepts a measurement value in inches and returns the equivalent of the measurement value in feet"""
def inchToFeetConverter(x):
    print(str(x) + ' -> ' + str(x*(1/12)))

inchToFeetConverter(1.5)
inchToFeetConverter(5)

"""Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers."""	
def oddVSeven(number):
    if (number % 2 == 0):
        print("even")
    else:
        print("odd")

oddVSeven(8)
oddVSeven(7)


"""Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them."""
def timeToSecondsConverter(hours, minutes):
    print(str(hours) + "," + str(minutes) + ' -> ' + str(hours*3600+minutes*60))

timeToSecondsConverter(3,5)