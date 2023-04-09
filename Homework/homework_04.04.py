# 1. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke. 

task = input("Please enter a name to know the relationship:   ")

dict_of_relations = {
"Darth Vader": "father",
"Leia": "sister",
"Han": "brother in law",
"R2D2":	"droid"
}

if task in dict_of_relations.keys():
    print("Luke, I am your" + " " + dict_of_relations[task] + "!")
else:
    print("Luke, you don't have such a relative!")


# 2. Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.

task =  input("Please enter damage number, speed and unit of speed: ")

damage = task.split(", ")
damage[0] = int(damage[0])
damage[1] = int(damage[1])
minutes_to_seconds = damage[1]*60
hours_to_seconds = damage[1]*3600
condition = damage[0]>=0 and damage[1]>=0

if condition == 1: # if condition == True
    if damage[2] == "second":
        print(damage[0]*damage[1])
    if damage[2] == "minute":
        print(damage[0]*minutes_to_seconds)
    if damage[2] == "hour":
        print(damage[0]*hours_to_seconds)
else:
    print("Invalid damage or speed") 

# 3. Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.

task = input("Please enter a list from integers and strings;    ")
filter_list = [1, 2, 3, "a", "b", 4]

# way 1
int_list = [i for i in filter_list if type(i)==int]

print(int_list)

# way 2

filter_list = [1, 2, 3, "a", "b", 4]
int_list = []

for item in filter_list: 
    if type(item) == int: 
        int_list.append(item)
print(int_list)

# 4. Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. 
# A number is symmetrical when it is the same as its reverse.

task = input("Please write a number to know if it is symmetrical or not:   ")

first_part = task[:(len(task)//2)]
second_part_even = task[(len(task))//2:]
second_part_even_reversed = second_part_even[::-1]
second_part_odd = task[((len(task)//2)+1):]
second_part_odd_reversed = second_part_odd[::-1]

if len(task)%2==0:
        if first_part == second_part_even_reversed:
            print("Is symmetrical")
if len(task)%2 != 0:
        if first_part == second_part_odd_reversed:
            print("Is symmetrical")
        else:
             print("Is not symmetrical")


# 5. Create a function that changes all the elements in a list as follows:

# Add 1 to all even integers, nothing to odd integers.
# Concatenates "!" to all strings and make the first letter of the word a capital letter.
# Changes all boolean values to its opposite.

task = [13, "13", "12", "twelve"] 

for item in task:
    if type(item)== int and item%2 == 0:
        print(item + 1)
    elif type(item)== int:
        print(item)
    if type(item) == str:
        print(item.capitalize()+ "!")
    if type(item)==bool:
        print(not bool(item))

# 6. Create a function that takes a string s and returns a list of two-paired characters.
# If the string has an odd number of characters, add an asterisk * in the final pair.

word = ""
list = []

if len(word) % 2 == 1:
    word += "*"

for i in range(0, len(word), 2):
    list.append(word[i:i+2])

print(list)


# 7. Create a function that takes two parameters and, if both parameters are strings, 
# add them as if they were integers or if the two parameters are integers, concatenate them.

parameters = (1, "2")

type_int = 0
type_str = 0

for i in parameters:
    if type(i) == str:
        type_str += 1
    if type(i) == int:
        type_int += 1


if type_int == 2:
    parameters_to_str = list(map(str,parameters))
    print("".join(parameters_to_str))
elif type_str == 2:
    parameters_to_int = list(map(int,parameters))
    print(sum(parameters_to_int))
else:
    print("None")   

# 8. Write a function that does the following operations: adding, subtracting, dividing, or multiplying values. 
# It is simply referred to as variable operation variable. Of course, the variables have to be defined, but in 
# this challenge the variables will be defined for you. All you have to do is look at the variables, do some string to integer 
# conversions, use some if conditionals, and combine them based on the operation.

operation = ("0", "5", "divide")
first_value = int(operation[0])
second_value = int(operation[1])

if operation[2]=="add":
    output = first_value + second_value
elif operation[2]=="subtract":
    output = first_value-second_value
elif operation[2]=="divide":
    if second_value == 0:
        output = "undefined"
    else:
        output = first_value // second_value
else:
    output = "undefined"

print(output)


# 9. Check if the given string consists of only letters and spaces and if every letter is in lower case.


word =  "Hello world?"
output = []

for letter in word:
    if letter.isspace():
        output.append(bool(letter))
    elif letter.isalpha():
        if letter.islower():
            output.append(bool(letter))
    

if len(word) != 0 and len(word) == len(output):
    print("True")
else:
    print("False")

# 10. Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, or neither.

check = [1, 1, 3]

if check == list(set(sorted(check))):
    print("increasing")
elif check == list(set(sorted(check)))[::-1]:
    print("decreasing")
else:
    print("neither")

