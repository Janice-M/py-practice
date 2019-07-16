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


for i in range(2995,3001):
    print("I love you " + str(i) + " Mr. Stark")

    #while loop


number = 0
while True:
    print("I love candy "+ str(number))
    number +=1
    if number == 7 :
        break   

# taken numbers
numTaken = [3,5,7,11,13]

print("Available numbers")

# loop
for i in range(1,21):
    if i in numTaken:
        continue
    print(i)
    list_a = ["a","b","c","d"] 
list_b = [1,2,3,4,5,6]

# Joining list_b to list_a

list_a.extend(list_b)

print(list_a) # this will print ["a","b","c","d",1,2,3,4,5,6]
print(list_b) # this will print [1,2,3,4,5,6]