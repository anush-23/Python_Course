# Create a function that takes a string and returns it as an integer

value = input("Write a string to return an integer:  ")
output = int(value)

print(value, "->" , output)


#Create a function that takes a boolean variable flag and returns it as a string.

value = bool(input("Write a boolean variable to return a string:  "))
output = str(value)

print(value, "->", output)


#Write a function that returns the string "something" joined with a space " " and the given argument a.

argument = input("input the a argument:  ")
string = "Something"

print(string, "", argument)

#Create a function that takes a string and returns the number (count) of vowels contained within it.

word = input("Type a word to count vowels in it:   ")

output = word.count("a")+word.count("e") + word.count("i") + \
    word.count("o")+word.count("u")

print(output)


#Write a function that takes a credit card number and only displays the last four characters. The rest of the card number must be replaced by ************.


acc_number = input("write your credit card number:  ")

print(acc_number.replace(acc_number[0:12],"************"))

#Create a function that replaces all the vowels in a string with a specified character.

str = input("Write a word to replace the vowels:   ")
str = str.replace("a", "#")
str = str.replace("e", "#")
atr = str.replace("i", "#")
str = str.replace("o", "#")
str = str.replace("u", "#")

print(str)

#Create a function that returns True if a given inequality expression is correct and False otherwise.

expression = input("Enter a valid expression and know if it is true or false: ")
print(eval(expression))


#Create a function that takes a string (will be a person's first and last name) and returns a string with the first and last name swapped.

full_name = input("Enter first and last names and get them swapped: ")
space_index = full_name.index(" ")
first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]
print(last_name + " " + first_name)



#Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

var = input("write the name to get the relation:  ")
data = {
    "Darth_Vader": "father",
    "Leia": "sister",
    "Han": "brother in law"
}

print("Luke, I am your " + data[var] + ".")



#additional
pin = input("Please enter a valid pin:   ")

print(("True" * (((len(pin) == 4) or (len(pin) == 6)) and pin.isdecimal())) or "Invalid pin!")