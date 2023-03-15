"""For this challenge, you are supposed to find the sum of the digits of a two-digit number."""

x = int(input("write a number to get the sum of its digits:  "))
print(str(x) + ' -> ' + str(x % 10 + x // 10))




"""A repdigit is a positive number composed out of the same digit. Create a function that takes an two-digit integer and returns whether it's a repdigit or not."""

x = int(input("write a number to check if it is repdigit:  "))
print(str(x) + ' -> ' + str(x % 10 == x // 10))


""" Write a function that takes an integer minutes and converts it to seconds."""

x = int(input("write minutes to convert it into seconds:  "))
print(str(x) + ' -> ' + str(x*60))



"""Create a function that takes the age in years and returns the age in days."""

x = int(input("write the age in years to get it in days:  "))
print(str(x) + ' -> ' + str(x*365))


"""Create a function that accepts a measurement value in inches and returns the equivalent of the measurement value in feet"""

x = float(input("write inches to convert into feet:  "))
print(str(x) + ' -> ' + str(x*(1/12)))

"""Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers."""	
x = float(input("write a number to check if it is odd or even:  "))

if (x % 2 == 0):
    print("even")
else:
    print("odd")


"""Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them."""

x = int(input("write the number for hours:  "))
y = int(input("write the number for minutes:  "))

print(str(x) + "," + str(y) + ' -> ' + str(x*3600+y*60))
