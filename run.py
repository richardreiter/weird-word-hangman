import random  # imports random library to pick a word randomly
import os  # imports os library so it can be used to help clear the screen
from words import weird_words  # imports weird word list from words.py file
from images import hanging_man  # imports hanging man dictionary from images.py file


# function to randomly choose a word from weird words list
def pick_word():
    actual_word = random.choice(weird_words)
    return actual_word.upper()


def play_game(actual_word):
    word_reveal = "_" * len(actual_word)
    user_guessed = False
    user_guessed_letters = []
    user_guessed_words = []
    user_tries = 6
    print("This is Only Weird Words Hangman, welcome amigo!")
    print(show_hangman(user_tries))
    print(word_reveal)
    print("\n")
    while not user_guessed and user_tries > 0:
        user_guess = input("Please guess a word or letter: ").upper()
        if len(user_guess) == 1 and guess.isalpha():
            if user_guess in user_guessed_letters:
                print("Sorry, but you've actually already guessed this letter!", user_guess)
            elif user_guess not in actual_word:
                print(user_guess, "is actually not in the word. :(")
                user_tries -= 1
                user_guessed_letters.append(user_guess)
            else:
                print("Nice one! ", user_guess, "is in the actual word!")


        elif len(user_guess) == len(actual_word) and user_guess.isalpha():
        
        else:
            print("Sorry, this guess was invalid, please try again! :)")
        print(show_hangman(user_tries))
        print(word_reveal)


# function to check user guess and reveal correct letters
def check_user_guess(letter, current_word):
    global show_word
    for i in range(0, len(current_word)):
        letter = current_word[i]
        if user_guess == letter:
            show_word[i] = user_guess
    if "_" not in show_word:
        return True  # function returns true if user wins
    else:
        return False  # else returns false


def game_status():  # function to help represent games current status
    os.system("clear")
    print(hanging_man[6-current_lives])
    print(" ".join([str(i) for i in show_word]))  # converts each list element into a string
    print("You've got", current_lives, "lives")  # prints how many lives the user currently has left


while match_won is False and current_lives > 0:  # game loop boolean
    game_status()
    user_guess = input("Pick a letter (or word if you're feeling lucky) and guess the hidden word:")  # ask user for guess input
    user_guess = user_guess.upper()  # method to convert string to upper

    if user_guess == current_word:  # conditional in case user gets the current word right
        match_won = True
        show_word = current_word
    if len(user_guess) == 1 and user_guess in current_word:  # implement single letter guess
        for i in range(0, len(current_word)):
            match_won = check_user_guess(user_guess, current_word)
    else:
        current_lives -= 1  # subtract one from current lives
        game_status()

if match_won:
    print("Nice one! You guessed the weird word =-O")
else:
    print(f"The man has been hung ¯\_(ツ)_/¯, the hidden word was actually {current_word}")
