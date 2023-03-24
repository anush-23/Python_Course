# 1. Create a function that takes a list containing only numbers and return the first element.

list = input('Please enter an element of the list:  ')

splitting = list.split(',')

print(splitting[0])

# 2.  Create a function that takes a list of numbers. Return the largest number in the list.

message = input('Please enter a list to know the largest number of it:  ')

res = message.split(',')

result = list(map(int, res))


print(max(result))

#one more way to solve

result.sort()

print(result[-1])


# 3. Create a function that takes a list of numbers and returns the smallest number in the list.

message = input('Please enter a list to know the smallest number of it:  ')

res = message.split(',')
result = list(map(int, res))

print(min(result))

 #one more way to solve

result.sort()

print(result[0])


4. Create a function that takes a list and returns the difference between the biggest and smallest numbers.

message = input('Please enter a list to know the difference between the biggest and smallest numbers: ')

res = message.split(',')
result = list(map(int, res))

print(max(result) - min(result))

#  one more way to solve

result.sort()

print(result[-1] - result[0])

# 5. Create a function to concatenate two integer lists.

first_list = input('Please enter an integer list:  ')
second_list = input('Please enter an integer list:  ')

res1 = first_list.split(',')
res2 = second_list.split(',')

result1 = list(map(int, res1))
result2 = list(map(int, res2))

print(result1 + result2)

# 6. Given a list of numbers, return True if the sum of the values in the list is less than 100; otherwise return False.

message = input('Please enter a list:  ')

res = message.split(',')

result = list(map(int, res))

print(result)
print(((sum(result) < 100) * 'true') or 'false')


# 7. Given a list of integers, determine whether the sum of its elements is even or odd.

message = input('Enter a list determine whether the sum of its elements is even or odd:  ')

res = message.split(',')
result = list(map(int, res))

summary = sum(result)

print((summary%2==0) * 'even' or 'odd')

# 8. Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

message =  input('Please enter a date MM/DD/YYYY to get it converted YYYYDDMM:   ')

res = message.split('/')
result = list(map(int, res))

result.reverse()

new_res = list(map(str, result))

print(''.join(new_res))

# another way to solve
print(new_res[0]+new_res[1]+new_res[2])

# 9. Create a function that takes two numbers as arguments num, length and returns a list of multiples of num until the list length reaches length.

message_1 =  7 #int(input('Please enter the num:   '))
message_2 =  5 #int(input('Please enter the length:   '))

list = [1] * message_2
list[0] = 7
list[-1] = 7*5
print(list)