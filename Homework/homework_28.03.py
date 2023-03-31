# 1. Given a list, rotate the values clockwise by one (the last value is sent to the first position).

request = input('Type a list to rotate the values clockwise by one:   ')

result = list(map(int, request.split(',')))

result.insert(0, result.pop(-1))


print(result)

# 2. Create a function that inverts the rgb values of a given tuple.

request = input("Write a tuple to inverts the rgb values: ")

tup = tuple(map(int, request.split(",")))

color_invert=(255-tup[0], 255-tup[1], 255-tup[2])

print(color_invert)

# 3. Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location
# in the list. If Bob is not in the list, return -1.

request = input('Write a list to find the index of the name "Bob" in it:   ')

splitting = list(map(str, request.split(', ')))

print(('Bob' not in splitting) * (-1) or splitting.index('Bob'))

# 6. Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.

dict = {}
dict['student 1'] = input('Write students names to return the names in alphabetical order:  \nstudent 1 ')
dict['student 2'] = input('student 2 ')
dict['student 3'] = input('student 3 ')


print(sorted(dict.values()))


# 9. Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])

# 10. Rename key of a dictionary
      # Write a program to rename a key city to a location in the following dictionary.

dic ={
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

dic.pop("city")

dic.update({"location": "New york",})

print(dic)
