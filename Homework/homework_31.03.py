# 1. Given three lists of integers: lst1, lst2, lst3, return the sum of integers which are common in all three lists.

lst = ([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2])

common_ints = [i for i in lst[0]
                   if i in lst[1]
                   and i in lst[2]]

print(sum(common_ints)) 

# 2. Write a function that takes a list of numbers and returns a list with two elements:
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.

lst = input("Please enter a list to count the sum of even and odd numbers of it:   ")
splitting = lst.split(", ")

str_to_int = list(map(int, splitting))

even_list =[]
odd_list =[]

for i in str_to_int:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

sum_even = sum(even_list)
sum_odd = sum(odd_list)

output = [sum_odd, sum_even]


print(output)


# 3. Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } 
# and[] returns a dictionary of objects like { "name": "John", "top_note": 5 }.

dict = { "name": "John", "notes": [3, 5, 4] }

dict["top_note"] = max(dict.pop('notes'))

print(dict)


# 5. You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. 
# You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), 
# and the starting inventory. Return the total profit made, rounded to the nearest dollar.

profit = {
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}

print(round((profit["sell_price"]-profit["cost_price"])*profit["inventory"]))


# 6. A number is said to be Harshad if it's exactly divisible by the sum of its digits.
# Create a function that determines whether a number is a Harshad or not.

harshad = input("Please enter a number to know if it is harshad:   ")

is_harshad = int(harshad) % len(harshad) == 0

print(is_harshad)

# 7. Given an input string, reverse the string word by word.

phrase = input("Please enter a phrase to get it reversed:   ")

rev = phrase.split(" ")
rev.reverse()
output = " ".join(rev)

print(output)


# 8. Create a function that builds a word from the scrambled letters contained in the first list. 
# Use the second list to establish each position of the letters in the first list. Return a string from the unscrambled letters (that made-up the word).


letters = ["e", "t", "s", "t"]
indexes = [3, 0, 2, 1]

word = list(map(letters.__getitem__, indexes))
print("".join(word))

# 9. Create a function to test if a string is a valid pin or not.

pin = input("Please enter a valid pin:  ")

print((len(pin) == 4 or len(pin) == 6) and pin.isdecimal())

# 10. Return a new set of identical items from two sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

output = set1.intersection(set2)

print(output)

# 11. Write a Python program to return a new set with unique items from both sets by removing duplicates.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

output = set1.union(set2)

print(output)

#12. Given two Python sets, write a Python program to update the first set with items that 
# exist only in the first set and not in the second set.

set1 = {10, 20, 30}
set2 = {20, 40, 50}

output = set1.difference(set2)

print(output)

# 13. Given an input string, reverse the string word by word (reversed word also).

phrase = input("Please enter a phrase to get it reversed:   ")

way 1: reversing = phrase[::-1]

way 2: reversing = "".join(list(reversed(phrase)))  

print(reversing)

