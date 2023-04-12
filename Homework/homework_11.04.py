# 1. Write a function that takes a string name and a number num (either 0 or 1) and return "Hello" + name if num is 1, otherwise return "Bye" + name.

def say_hello_bye(name: str, num: int):

    if num == 1:
        return "Hello" + " " + name.capitalize() + "!"
    elif num == 0:
        return "Bye" + " " + name.capitalize() + "!"
    else:
        return "Wrong input"
    

# 2. Create a function that takes a list (slot machine outcome) and returns True if all elements in the list are identical, and False otherwise.
# The list will contain 4 elements.

def test_jackpot(element: list):
    
    for item in element:
        if  item !=  element[0]:
            return False
    else:
        return True
        


# 3. Create a function that takes an array of hurdle heights and a jumper's jump height, and determine whether or not the hurdler
#  can clear all the hurdles.
# A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.

def hurdle_jump(hurdle_hight, jump_height):
    
    for item in hurdle_hight:
        if item > jump_height:
            return False
            break
        else:
            return True
        

# 4. Create a function that takes a number as its argument and returns a list of all its factors.

def factorize(number):
    out = []
    for item in range(1,  number + 1):
        if number % item == 0:
             out.append(item)
    return out



# 5. Create a function that returns the number of palindrome numbers in a specified range (inclusive).

def is_palindrome(number):
    if number in range(1, 10):
        return True
    elif str(number) == (str(number) [::-1]):
        return True
    else:
        return False
    

def count_palindromes(start, end):
    out = []
    for item in range(start, end + 1):
        if is_palindrome(item) == True:
            out.append(item)
    return len(out)


# 6. Write a function that takes a string, breaks it up and returns it with vowels first, 
# consonants second. For any character that's not a vowel (like special characters or spaces), treat them like consonants.

def is_vowel(letter):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    if letter in vowel_list:
        return True
    else:
        return False
    

def vowels_first(expression):
    
    vowels = ""

    for letter in expression:
        if is_vowel(letter) == True:
            vowels += letter
            expression = expression[:expression.index(letter)] + expression[expression.index(letter)+1:]

    return vowels + expression
        


# 7. Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.

def hacker_speak(expression: str):
   
    letter_to_symbol = {
    "a": 4,
    "e": 3,
    "i": 1,
    "o": 0,
    "s": 5
    }

    letter_to_symbol = {key: str(value) for key, value in letter_to_symbol.items()}

    for i in letter_to_symbol:
        expression = expression.replace(i, letter_to_symbol[i])
    
    return expression



# 8. Create a function that takes an integer and returns it as an ordinal number. An Ordinal Number is a number that tells 
# the position of something in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.

def return_end_of_number(number):


    last_item = int(str(number)[-1])
    last_two_items = int(str(number)[-2:])


    if last_item == 1 and last_two_items != 11:
        print(str(number) + "-" + "st")
    elif last_item == 2 and last_two_items != 12:
        print(str(number) + "-" + "nd")
    elif last_item == 3 and last_two_items != 13:
        print(str(number) + "-" + "rd")

    else:
        print(str(number) + "-" + "th")


# 9. Create a function that converts Celsius to Fahrenheit and vice versa.

def convert_celsius_farenheit(argument: str):

    if argument[-1] == "C":
        formula_celsius_to_farenheit = round(int(argument[:-2])*1.8+32)
        return str(formula_celsius_to_farenheit) + "*F"
    if argument[-1] == "F":
        formula_farenheit_to_celsius = round((int(argument[:-2])-32)*5/9)
        return str(formula_farenheit_to_celsius) + "*C"
    else:
        return "Error"
    

# 10. Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. 
# The RNA will be represented as a string containing only the characters "A", "C", "G" and "U". 
# Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:

def reverse_complement(RNA: str):

    converted = ""
    pairing = {
        "A": "U",
        "U": "A",
        "G": "C",
        "C": "G"
        }
    for item in RNA:
        converted += pairing[item]

    return converted[::-1]


# 11. Create a function to perform basic arithmetic operations that includes addition,
#  subtraction, multiplication and division on a string number
# (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").



def arithmetic_operation(expression):
    
    splitted = expression.split(" ")
    
    operand_1 = int(splitted[0])
    operand_2 = int(splitted[2])
    operator = splitted[1]
    
    if operator == "+":
        result = operand_1 + operand_2
    elif operator == "-":
        result = operand_1 - operand_2
    elif operator == "*":
        result = operand_1 * operand_2
    elif operator == "//":
        if operand_2 == 0:
            result = -1
        else:
            result = operand_2 / operand_1