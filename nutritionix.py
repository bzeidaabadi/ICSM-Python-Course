#nutritionix EXERCISE - POST

import requests
import json

endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

APP_id = 'b26a12aa'
APP_key = 'f895658d2011a221a07d40d9cba7400a'

headers = {'x-app-id':APP_id, 'x-app-key':APP_key }
parameters = {'query': 'I cycled 6 minutes to park and back for a total of 4 kilometers. At the park I ran 2 miles in 14 minutes',
              'gender': 'male',
              'weight_kg': 72,
              'height_cm': 178,
              'age': 21}

response = requests.post(endpoint, json= parameters, headers = headers)
print(response)
print(response.json())

total_calories = 0
exercise_list = response.json()['exercises']
# print(exercise_list)
#calories burned per exercise
for exercise in exercise_list:
    total_calories += exercise['nf_calories']
    
    print(f"you burnt {exercise['nf_calories']} calories doing {exercise['name']}")
print(f"total calories burnt today: {total_calories}")


#nutritionix food lookup - GET 
import requests

# Set the API endpoint and the required headers
APP_id = 'b26a12aa'
APP_key = 'f895658d2011a221a07d40d9cba7400a'

endpoint = 'https://trackapi.nutritionix.com/v2/search/instant'

headers = {'x-app-id': APP_id, 'x-app-key': APP_key}

# Set the parameters for the request
parameters = {'query': 'lemon'}

# Make the GET request
response = requests.get(endpoint, params=parameters, headers=headers)

# Print the response status code to check for success
#print(response.status_code)

#common vs branded

# print(response.json()['common'])
food_name = response.json()['branded'][0]['food_name']

food_calorie = response.json()['branded'][0]['nf_calories']

print(food_calorie)



# # Check the response status code to make sure the request was successful
# if response.status_code == 200:
#     # Get the first food in the list of matching foods
#     food = response.json()['branded'][0]
    
#     # Print the food's name and calorie count
#     print(f"{food['food_name']}: {food['nf_calories']} calories")
# else:
#     # Print an error message if the request was not successful
#     print("An error occurred while fetching the food information")
    
    

#nutritionix food lookup - POST 

import requests
import json

# Set API endpoint, app ID, and app key
endpoint = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

APP_id = 'b26a12aa'
APP_key = 'f895658d2011a221a07d40d9cba7400a'

# Set header
headers = {
  'Content-Type': 'application/json',
  'x-app-id': APP_id,
  'x-app-key': APP_key
}

# Set request body (if applicable)
parameter = {'query': 'I had a two chicken breasts with some rice and apple juice'}

# Make POST request
response = requests.post(endpoint, json= parameter, headers = headers)

print(response.json())
#print(help(response))

total_calories_2 = 0
food_list = response.json()['foods']
#calories consumed
for food in food_list:
    total_calories_2 += food['nf_calories']
    
    print(f"you consumed {food['nf_calories']} calories when you had {food['food_name']}")
print(f"total calories consumed today: {total_calories_2}")


total_sugar = 0
food_list = response.json()['foods']
#sugar consumed
for food in food_list:
    if isinstance(food['nf_sugars'], float):
        total_sugar += food['nf_sugars']
    
        print(f"you consumed {food['nf_sugars']} grams of sugar when you had {food['food_name']}")
print(f"total grams of sugar consumed today: {total_sugar}")


#make function to keep DRY

# def counter(response_key, field):
#   # Extract desired information from response
#   nutrition_info_list = response.json()[response_key]

#   total = 0
#   for item in nutrition_info_list:
#     # Only include item in calculation if field value is a float
#     if isinstance(item[field], (float, int)):
#       total += item[field]
#       if response_key == 'foods':
#         if field == 'nf_calories':
#           print(f"you consumed {item[field]} calories when you had {item['food_name']}")
#         elif field == 'nf_sugars':
#           print(f"you consumed {item[field]} grams of sugar when you had {item['food_name']}")
#       elif response_key == 'exercises':
#         print(f"you burnt {item[field]} calories doing {item['name']}")
#   if response_key == 'foods':
#     if field == 'nf_calories':
#       print(f"total calories consumed today: {total}")
#     elif field == 'nf_sugars':
#       print(f"total grams of sugar consumed today: {total}")
#   elif response_key == 'exercises':
#     print(f"total calories burnt today: {total}")

# # Example usage:
# counter('foods', 'nf_calories')
# counter('foods', 'nf_sugars')
# #counter('exercises', 'nf_calories')

