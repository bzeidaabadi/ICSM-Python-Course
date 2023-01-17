import random

def LL_flashcards():
  #create dictioanry
  dictionary = {'vastus medaialis': 'femoral nerve', 'soleus': 'tibial nerve', 'fhl': 'tibial nerve', 'gracilis': 'obturator nerve'}

  # Create a list of the keys in the dictionary
  keys = list(dictionary.keys())
  #[vastus..., soleus, fhl,]
  # Shuffle the list of keys
  #random.shuffle(keys)
  # Iterate through the list of keys and ask the user to identify the corresponding value
  for key in keys:
    # Ask the user to identify the value
    user_answer = input(f"What is the innervation of {key} muscle?")
    # Check if the user's answer is correct
    if user_answer.lower() == dictionary[key].lower():
      # If the answer is correct, print a message
      print(f"Nice one! {key} is innervated by the {dictionary[key]} ")
    ##elif user_answer.lower() == 'done':
        #break
    else:
      # If the answer is incorrect, print the correct answer
      print(f"Ooof not quite. {key} is innervated by the {dictionary[key]}.")

# Test the function with the example dictionary

LL_flashcards()





