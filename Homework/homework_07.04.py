# 1. Write a function that takes a string name and a number num (either 0 or 1) and return 
# "Hello" + name if num is 1, otherwise return "Bye" + name.

hello_bye = ("jose", 0)


if hello_bye[1]==1:
    output = "Hello" + " " + hello_bye[0].capitalize() + "!"
elif hello_bye[1]==0:
    output = "Bye" + " " + hello_bye[0].capitalize() + "!"

print(output)

# 2. Create a function that takes a list (slot machine outcome) and returns True if all elements 
# in the list are identical, and False otherwise. The list will contain 4 elements.

test_jackpot = ["SS", "SS", "SS", "Ss"]

element = test_jackpot[0]
outcome = True
# way 1
for item in test_jackpot:
    if item == element:
        outcome = True
    else:
        outcome = False


print(outcome)

# way 2

test_jackpot = ["&&", "&", "&&&", "&&&&"]

element = test_jackpot[0]
outcome = True

for item in test_jackpot:
    if item != element:
        outcome = False
        break

print(outcome)

# 3. Create a function that takes an array of hurdle heights and a jumper's jump height, 
# and determine whether or not the hurdler can clear all the hurdles.
# A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.

height_jump = ([1, 2, 1], 1)

jump = height_jump[1]
hurdle_height = height_jump[0]

outcome = True

for item in hurdle_height:
    if item > jump:
        outcome = False
        break
  

print(outcome)

# 4. Create a function that takes a number as its argument and returns a list of all its factors.

number = 17
factorize = []

range_list = list(range(1,number + 1))

for i in range_list:
    if number % i == 0:
        factorize.append(i)

print(factorize)


