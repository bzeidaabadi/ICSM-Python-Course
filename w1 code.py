# identifying class of variables
# strings
x = "Hello, world!"
print(type(x))  # Output: <class 'str'>


# integers 
x = 42
print(type(x))  # Output: <class 'int'>


# floats 
x = 1.88
print(type(x))  # Output: <class 'float'>

# 
# booleans
#1
x = 5
y = 3

result = x > y
print(result)  # Output: True

#2
x = 5
y = 3

result = (x > y) and (x < 10)
print(result)  # Output: True

#3
x = 5
y = 3
z = 8

result = (x < y) and ((y < z) or (z < x))
print(result)  # Output: false

#3
x = 5
y = 3
z = 8

result = (x > y) and ((y < z) or (z < x)) and (z % 2 == 0)
print(result)  # Output: True

#4
x = 5
y = 3
z = 8

result = (x > y) and ((y < z) or (z < x)) and (z % 2 == 0)
print(result)  # Output: True


#print
# \n - new linw
# \t - tab
# \" - double quotes

#input
name = input("What is your name? ")
print(f"Hello, {name}!")

#f-string - .format
age = input("How old are you? ")
print("You are {} years old.".format(age))

#f-string easier way
height = float(input("Enter height in metres: "))
weight = float(input("Enter weight in Kg: "))
BMI = round(weight / (height ** 2),1)
print(f"Your BMI is: {BMI}.")


# mathematical operators - \  *  +  -  **  \\  % ==. ≠. >. <. ⇒  ≤

#if vs elif vs else

age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


grade = int(input("Enter your grade: "))
if grade >= 90:
    print("You got an A.")
elif grade >= 80:
    print("You got a B.")
elif grade >= 70:
    print("You got a C.")
else:
    print("You got a failing grade.")
    
    
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


symptoms = input("Enter your symptoms: ")
if "SOB" in symptoms and "cough" in symptoms:
    print("You may have a respiratory infection. See your GP")
elif "stomach pain" in symptoms and "vomiting" in symptoms:
    print("You may have a stomach bug. Drink plenty of fluids.")
elif "headache" in symptoms and "nausea" in symptoms:
    print("You may have a migraine. Take over-the-counter pain medication and see a doctor if your symptoms persist.")
else:
    print("Not sure what's going on, go see your GP")




