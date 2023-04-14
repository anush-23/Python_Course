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
    
    for item in range(len(new_expression)):
        if new_expression[item] == "a":
           new_expression[item] = new_expression[item].replace("a", "an absolute")
        elif new_expression[item] == "A":
            new_expression[item] = new_expression[item].replace("A", "An absolute")
        return " ".join(new_expression)
    

    

