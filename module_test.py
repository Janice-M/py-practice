import sys

name = sys.argv[1]
last = sys.argv[2]
age = sys.argv[3]

print(name)
print(last)
print(age)
# how sys works

# below is a check for nothing thing
babe = ""
list_a = []

if list_a:
    print("I will not run")
else:
    print("Grey Worm says you are empty")

    # loop codes


for i in range(2995, 3001):
    print("I love you " + str(i) + " Mr. Stark")

    # while loop


number = 0
while True:
    print("I love candy " + str(number))
    number += 1
    if number == 7:
        break

# taken numbers
numTaken = [3, 5, 7, 11, 13]

print("Available numbers")

# loop
for i in range(1, 21):
    if i in numTaken:
        continue
    print(i)
    list_a = ["a", "b", "c", "d"]
list_b = [1, 2, 3, 4, 5, 6]

# Joining list_b to list_a

list_a.extend(list_b)

print(list_a)  # this will print ["a","b","c","d",1,2,3,4,5,6]
print(list_b)  # this will print [1,2,3,4,5,6]
# Creating empty dictionaries
my_dict = {}
my_dict = dict()

# Creating a dictionary with keys and values
my_cat = {'name': ' Ser Pounce', 'age': 18, 'color': 'black'}
cat_name = my_cat['name']
print(cat_name)  # ' Ser Pounce'
birthdays = {"John": "August 1", "Marcus": "April 8"}
birthdays["mary"] = "September 14"
# this prints {"John":"August 1","Marcus":"April 8","Mary":"September 14"}
print(birthdays)
birthday = {"John": "August 1", "Marcus": "April 8", "Mary": "September 14"}

print(birthday.keys())  # this prints dict_keys(['John', 'Marcus', 'Mary'])


print("Enter a string")

input_string = input()

characters = {}

for character in input_string:
    characters.setdefault(character, 0)
    characters[character] = characters[character] + 1

print(characters)


#string formatting 
#The f before the string stands for f-strings or formatted strings and 
# allow us to put replacement fields {} with variable names inside our strings
name = "Grey Worm"
age = 9

print(f"My name is {name} and I am {age} years old")
#raw string 
print('Beyonce\'s lemonade stand')
    
alpha = "I like old music"
password = "K34jndnks"
number_string = "12345"
tabbs = "       "
titles = "I Love Cups"
false_titles = "I love Cups"

print( alpha.isalpha() )
print( password.isalnum() )
print( number_string.isdecimal() )
print( tabbs.isspace() )
print( titles.istitle() )
print( false_titles.istitle())

colon = "James"
sage = 19

print("My name is " + colon + " I am " + str(sage) + " years old")

#A slice statement is enclosed with [] square brackets and has two parts first is the position where to start slicing 
# and second is the position to stop but not including that position.
salamu = 'Hello, Moringa!'

part_one = salamu[0:5]
print(part_one)

number = [1,2,3,4,5,6,7,8,9]
four_digits = number[:4]
print(four_digits)
