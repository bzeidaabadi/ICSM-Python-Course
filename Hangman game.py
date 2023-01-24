import random

# Choose a random word from a list of words
words = ["dysdiadochokinesia", "ataxia", "nystagmus", "tremor", "staccato", "hypotonia"]
word = random.choice(words)

def hangman(word):
    # Set the number of lives
    lives = 6

    # Convert the word to a list of characters
    word = list(word)

    # Create a list of underscores the same length as the word
    guess = ["_"] * len(word)

    # Set up a list to store the letters that have been guessed
    letters_guessed = []

    # Start the game loop
    while lives > 0:
        # Print the current status of the game
        print("Current word: ", " ".join(guess))
        print("Letters guessed: ", " ".join(letters_guessed))
        print("Lives remaining: ", lives)

        # Prompt the user for a letter
        letter = input("Guess a letter: ")

        # Add the letter to the list of letters guessed
        letters_guessed.append(letter)

        # Check if the letter is in the word
        if letter in word:
            # If it is, update the list of underscores with the correct letter
            for i in range(len(word)):
                if word[i] == letter:
                    guess[i] = letter
        else:
            # If it's not, subtract one from the number of lives
            lives -= 1

        # Check if the word has been completely guessed
        if "".join(guess) == "".join(word):
            print("Nice one!: ", "".join(word))
            break
    else:
        # If the loop ends and the word hasn't been completely guessed, the player loses
        print("You're bad mate. The word was: ", "".join(word))


# Start the game
hangman(word)


#two user (hard)
def hangman2():
  # Player 1 inputs a word
  word = input("Player 1, please enter a word for Player 2 to guess: ")
  
  # Initialize the game state
  lives = 6
  guessed_letters = []
  word_letters = set(word)
  
  # Player 2 starts guessing letters
  while lives > 0:
    # Display the current game state
    print("Lives: {}".format(lives))
    print("Guessed letters: {}".format(" ".join(guessed_letters)))
    print("Word: {}".format(" ".join(letter if letter in guessed_letters else "_" for letter in word)))
    
    # Player 2 makes a guess
    guess = input("Player 2, please enter your guess: ")
    if guess in word_letters:
      print("Correct! The word contains the letter '{}'.".format(guess))
      word_letters.remove(guess)
    else:
      print("Incorrect guess, try again.")
      lives -= 1
      
    # Update the list of guessed letters
    guessed_letters.append(guess)
    
    # Check if Player 2 has guessed all the letters in the word
    if  len(word_letters) == 0:
      print("Nice one! You have correctly guessed the word '{}'.".format(word))
      return
      
  # If Player 2 runs out of lives, the game is over
  print("You have run out of lives. The correct word was '{}'.".format(word))

# Start the game
hangman2()


x = round(123, -2)
y = str(x)
z = y[-2]
print(x)




print(round(123, -2))