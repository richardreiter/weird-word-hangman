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
