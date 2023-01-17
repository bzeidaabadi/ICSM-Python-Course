#list 
mylist = [1,2,3,4,5]
print(mylist[0])
#print(mylist[5])
print(mylist[-2])


# Append a new element to the end of the list using the append() method
mylist.append(6)
print(mylist)  # prints [1, 2, 3, 4, 5, 6]

# Remove the first occurrence of a given element from the list using the remove() method
mylist.remove(3)
print(mylist)  # prints [1, 2, 4, 5, 6]

# Get the length of the list using the len() function
length = len(mylist)
print(length)  # prints 6


# Count the number of occurrences of a given element in the list using the count() method
count = mylist.count(5)
print(count)  # prints 1

# Sort the elements of the list in ascending order using the sort() method
mylist.sort()
mylist.sort(reverse = True)
print(mylist)  # prints [1, 2, 4, 5, 6]

# Insert a new element at a specific index in the list using the insert() method
mylist.insert(2, 3)
print(mylist)  # prints [1, 2, 3, 4, 5, 6]


#string
mystring = 'ICSM Python'
mystring_lower = mystring.lower()
print(len(mystring))
print(mystring_lower[3])


#slicing
#start - inclusive
#stop - exclusive
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get a sublist containing the 3rd, 4th, and 5th elements of the list
sublist = numbers[2:5]
print(sublist)  # prints [3, 4, 5]


# Get a sublist containing every other element of the list, starting from the 2nd element
sublist = numbers[1::2]
print(sublist)  


# Get a sublist containing the last 3 elements of the list in reverse order
sublist = numbers[-1:-4:-1]
print(sublist)  

#reverse

print(numbers[::-1])


#dictionary

mydict = {'name': 'BZ', 'age': 20, 'course': 'MBBS'}

# Get the length of the dictionary using the len() function
length = len(mydict)
print(length)  # prints 3

# Check if a key exists in the dictionary using the in keyword
print('name' in mydict)  # prints True
print('uni' in mydict)  # prints False

# Get a list of the keys in the dictionary using the keys() method
keys = mydict.keys()
print(keys)  

# Get a list of the values in the dictionary using the values() method
values = mydict.values()
print(values)  

# Get a list of the key-value pairs in the dictionary using the items() method
items = mydict.items()
print(items)  

# Remove a key-value pair from the dictionary using the pop() method
my_dict_2 = mydict.pop('course')
print(my_dict_2)  

# Add a new key-value pair to the dictionary
mydict['university'] = 'ICL'

# Modify the value associated with an existing key in the dictionary
mydict['age'] = 21

# Print the entire dictionary
print(mydict)  

#EXAMPLE DATABASE
patient_dict = {
    'patient_id': 12345,
    'first_name': 'Zeric',
    'last_name': 'Zmith',
    'date_of_birth': '1970-01-01',
    'gender': 'male',
    'ethnicity':'black asian',
    'address': '52 Harley St',
    'phone_number': '079',
    'emergency_contact': {
        'name': 'Zemily Zmith',
        'relationship': 'sister',
        'phone_number': '078'
    },
    'medical_history': [
        {
            'condition': 'hypertension',
            'diagnosed_date': '2010-01-01',
            'medication': 'amlodipine 5mg'
        },
        {
            'condition': 'T2D',
            'diagnosed_date': '2012-01-01',
            'treatment': 'metformin 500mg'
        }
    ]
}




# Get the relationship of the emergency contact
relationship = patient_dict['emergency_contact']['relationship']
print(relationship) 

# Get the treatment for the first medical condition
treatment = patient_dict['medical_history'][0]['medication']
print(treatment)


#for loop - star sign
# starsignlist = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']
# monthlist = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# newlist = []
# #range() (start,stop,step)
# for i in range(len(starsignlist)):
#     month = monthlist[i]
#     sign = starsignlist[i]
#     newlist.append((month, sign))
    
# print(newlist)
#len(starsignlist)

import random

names = ["Zephyrine Zinnober", "Xanthe Xylaria", "Boroumand Zeidaabadi"]

for name in names:
    first_name, last_name = name.split()
    first_initial = first_name[0].lower()
    second_initial = last_name[0].lower()
    random_number = str(random.randint(1,9))
    email = first_initial + second_initial + random_number + "20@ic.ac.uk"
    print(email)

    
#while vs for loop
# Using a while loop to print the numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# Using a for loop to print the numbers from 1 to 10
for i in range(1, 11):
    print(i)
    
# Initialize a list of names
names = ['John', 'Alice', 'Bob', 'Charlie', 'Eve']

# Use a while loop to iterate over the list of names
i = 0
while i < len(names):
    name = names[i]
    print(name)
    #i = i + 1
    i += 1

# Use a for loop to iterate over the list of names
for name in names:
    print(name)
    
#can be used together but I will show this in week 4
