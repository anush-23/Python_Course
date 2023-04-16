# 1. Create a function which returns the number of true values there are in an array.

def count_true(argument):
   
    """ Counts the number of True values.
    Argument is a list of boolean values"""

    for item in argument:
        if item == True:
            return argument.count(True)
   
    return "0"


# 2. Create a function that validates whether a number n is within the bounds of lower and upper. Return false if n is not an integer.
        
def int_within_bounds(number, lower_bound, upper_bound):

    """ Returns true if number is within the bounds of lower and upper bounds and is integer"""

    if number > lower_bound and number < upper_bound and isinstance(number, int):
        return True
    
    return False

# 3. Create a function that takes three values: h hours, m minutes, s seconds
# Return the value that's the longest duration.


def longest_time(hours, minutes, seconds):

    """Returns the longest duration of given number of hours, minutes and seconds"""
    
    hour_to_second = hours * 3600
    minute_to_second = minutes * 60

    dict = {
        hour_to_second: hours,
        minute_to_second: minutes,
        seconds: seconds
    }

    comparison = max(dict.keys())
    
    for item in dict.keys():
        return  dict[comparison]
    
# 4. Create a function that takes the month and year (as integers) and returns the number 

def days(month, year):

    months_to_days = {
        "january": 31,
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31
    }
    
    if year % 4 == 0 and year % 100 != 0:
        months_to_days["february"] = 29
    else:
        months_to_days["february"] = 28
    
    return months_to_days[month]

# 5. Create a function that takes a string and censors words over four characters with *.

def censor(expression):
    new_expression = expression.split()
    
    for item in range(len(new_expression)):
        
        if len(new_expression[item]) > 4:

            new_expression[item] = "*" * len(new_expression[item])
    
    return " ".join(new_expression)


# 6. Given a sentence, create a function that replaces every "a" as an article with "an absolute".
#  It should return the same string without any change if it doesn't have any "a".
    
def absolute(expression):
    new_expression = expression.split()
    
    for i in range(len(new_expression)):
        if new_expression[i] == "a":
           new_expression[i] = "an absolute"
        elif new_expression[i] == "A":
            new_expression[i] = "An absolute"
    return " ".join(new_expression)
    

# 7. Return an Array of Subarrays
# Write a function that takes three arguments (x, y, z) and returns an array containing x subarrays (e.g. [[], [], []]), 
# each containing y number of item z.

# x Number of subarrays contained within the main array.
# y Number of items contained within each subarray.
# z Item contained within each subarray.

def matrix(x, y, z):
    new_list = []

    for i in range(x):
        sub_list = []
        for j in range(y):
            sub_list.append(z)

        new_list.append(sub_list)
   
    return (new_list)

print(matrix(3, 2, 0))


# 8. Given a string of numbers separated by a comma and space, return the product of the numbers.

def multiply_nums (nums):
    result = 1
    nums = nums.split(", ")
    
    for item in nums:
        result *= int(item)
    return result


# 9. Create a function that takes a string road and returns the car that's in first place. The road will be made of "=", 
# and cars will be represented by letters in the alphabet.


def first_place(expression):
    output = ""
    
    if "=" not in expression:
        return "No road available"
    
    for letter in expression[::-1]:
        if letter != "=":
            return letter
            
        
    return "No car available"


# 10. Create a function that takes an array of numbers between 1 and 10 (excluding one number) and returns the missing number.


def missing_num(array_of_numbers: list):
    
    array_to_compare = list(range(1, 11))
    
    for item in array_to_compare:
        if item not in array_of_numbers:
            return item
    
