import random  # imports random library to pick a word randomly
from words import weird_words  # imports weird word list from words.py file


# function to randomly choose a word from weird words list
def pick_word():
    actual_word = random.choice(weird_words)
    return actual_word.upper()


# make a list of underscores of current word's length
current_word = "TEST"
show_word = list(len(current_word)*"_")
print(show_word)
current_lives = 6  # number of lives
match_won = False


while match_won == False and current_lives > 0: #  game loop boolean
    user_guess = input("Pick a letter (or word if you're feeling lucky) and guess the hidden word:") # ask user for guess input
    user_guess = user_guess.upper()  # method to convert string to upper
    
    if user_guess == current_word: # conditional in case user gets the current word right
        match_won = True
    else:
        current_lives -= 1 #  subtract one from current lives

if match_won:
    print("Nice one! You guessed the weird word :-O")
else:
    print(f"The man has been hung :(, the hidden word was actually {current_word}")