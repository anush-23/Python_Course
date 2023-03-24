"""Create a function that returns True if an integer is evenly divisible by 5, and False otherwise"""

number = -16

print("true" * (number % 5 == 0) or "false")

"""Emmy has written a function that returns a greeting to users. However, she's in love with Mubashir, and would like to greet him slightly differently. 
She added a special case in her function, but she made a mistake."""

name = "Michael"

print((name == "Mushabir") * ("Hello my love!") +
      (name != "Mushabir") * ("Hello" + " " + name + "!"))


"""Create a function that takes two arguments. Both arguments are integers, a and b. Return True if one of them is 10 or if their sum is 10."""

number1 = 4
number2 = 6

print(((number1+number2) == 10 or number1 ==
      10 or number2 == 10) * "true" or "false")

""" Create a function that takes a string txt and a number n and returns the repeated string n number of times. If given argument txt is not a string, return Not A String !!"""

name = 10
count = 4
print((type(name) == str) * name*count or "Not a string")

""" Given a string, return True if its length is even or False if the length is odd."""

text = "Asatur"

print((len(text) % 2 == 0)*"true" or "false")


"""Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters Create a function that takes two strings as arguments and return either True or False 
depending on whether the total number of characters in the first string is equal to the total number of characters in the second string"""

text1 = "ABCD"
text2 = "ABC"

print((len(text1) == len(text2)) * "true" or "false")
