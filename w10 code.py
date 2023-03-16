#what is API?
#get, put, post, delete
#request.ok


#1 
import requests
response = requests.get('https://api.chucknorris.io/jokes/random')
print(response.ok)
print(response.status_code)


# Check the status code to make sure the request was successful
if response.status_code == 200:
  # Get the joke from the response
  joke = response.json()['value']
  print(joke)
else:
  print('Sorry, there was an error')
  
  
  


  
# 2 category
import requests
endpoint = 'https://api.chucknorris.io/jokes/categories'

# Make the API request
response = requests.get(endpoint)

# Check the status code to make sure the request was successful
if response.status_code == 200:
  # Get the list of categories from the response
  categories = response.json()
  print(categories)
else:
  print('Sorry, there was an error getting the list of categories from the Chuck Norris Facts API')
  

import requests

# 3Make a request to the Chuck Norris Facts API

endpoint = 'https://api.chucknorris.io/jokes/random'
params = {'category': 'science'}

# Make the API request
response = requests.get(endpoint, params=params)
if response.status_code == 200:
  # Get the joke from the response
  joke = response.json()['value']
  print(joke)
else:
  print('Sorry, there was an error getting a joke ')
  

  

  
  
  