#sets
# Creating a set using the set() function
numbers = set([1, 2, 3, 4, 5])
print(numbers)  # Output: {1, 2, 3, 4, 5}

# Creating a set using curly braces
letters = {'a', 'b', 'c', 'd'}
print(letters)  # Output: {'a', 'c', 'b', 'd'} random

# Adding an element to a set
letters.add('e')
print(letters)  # Output: {'a', 'c', 'b', 'd', 'e'}

# Removing an element from a set
letters.remove('b')
print(letters)  # Output: {'a', 'c', 'd', 'e'}

#uses

# Performing the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1.union(set2)
print(union)  # Output: {1, 2, 3, 4, 5}

# Performing the intersection of two sets
intersection = set1.intersection(set2)
print(intersection)  # Output: {3}

# Performing the difference of two sets. what is present in set one that is not present in set 2
difference = set1.difference(set2)
print(difference)  # Output: {1, 2}


#tuples
# Creating a tuple
coordinates = (4, 5)
print(coordinates)  # Output: (4, 5)

# Creating a tuple with multiple elements
colors = ('red', 'green', 'blue')
print(colors)  # Output: ('red', 'green', 'blue')

# Accessing elements of a tuple using indexing
print(colors[0])  # Output: 'red'
print(colors[2])  # Output: 'blue'

# Trying to modify an element of a tuple
colors[0] = 'orange'  # This will raise a TypeError


#functions
#long code
weight = 70  # in kilograms
height = 1.75  # in meters
bmi = weight / (height ** 2)
print(bmi)  # Output: 22.957446808510638


def calculate_bmi():
    weight = float(input("What is your weight in Kg?"))
    height  = float(input("what is your height in metres?"))
    BMI = weight / (height ** 2)
    print(round(BMI,1))

#call function
calculate_bmi()

def calculate_bmi2(weight, height):
    weight = float(weight)
    height  = float(height)
    print(round(weight / (height ** 2),2))

#call function

bmi = calculate_bmi2(70, 1.75)




#rounding
a = round(324,1)
#positive - decimal places
#negative - sig fig from decimal point

#scope - global local
# Global variable
x = 10

def func():
    # Local variable
    y = 5
    print(x, y)  # Output: 10 5

func()
print(x)  # Output: 10
#print(y)  # This will raise a NameError because y is a local variable




#default 
def greet(name, greeting="Hello"):
    print(greeting + ", " + name)

greet("John")  # prints "Hello, John"
greet("Jane", greeting="Hi")  # prints "Hi, Jane"


#keyword
def greet(name, greeting):
    print(greeting + ", " + name)

greet(name="John", greeting="Hello")  # prints "Hello, John"
greet(greeting="Hi", name="Jane")  # prints "Hi, Jane"


#recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(6)
print(result)# result is 120

