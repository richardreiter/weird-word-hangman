# WEIRD WORD HANGMAN

[Weird Word Hangman](https://github.com/richardreiter/hangman) is a Python terminal based word guessing game, which runs on Code Institute's mock terminal on Heroku.

There's a hidden weird word and the player needs to guess a letter (or the whole word) in each round.

The player has 6 lives, each wrong guess deducts a life from the player. If the player runs out of lives they hang the man and the player loses.

The player wins the game if they correctly identify all the hidden letters!

![Responsive Weird Word Hangman](docs/screenshots/wwh-responsiveness.png)

Visit the live project [here.](https://weird-word-hangman.herokuapp.com/)

## UX (User Experience)

### Project Goals

- Showcase a simple classic fun game.
- Provide the user with instructions/rules on how to play the game.
- Provide feedback to the user on each round.

### Target Audience

- People of all ages.
- Anyone who wants to have a bit of fun with a guessing game.

### User Stories

- As a user, I want to understand what the game is about.
- As a user, I want to know how to play the game.
- As a user, I want to know the game's rules.

## Features

### Existing Features

- __Welcome Screen__

  - This is the first screen the player sees, it welcomes the player with the game rules. 
  - At the end of the welcome message it prompts the player to input their name.

![Welcome Screen](docs/screenshots/wwh-welcome.png)

- __Main Screen__

  - Greets the player with their chosen name.
  - Displays the image of the hanging man state.
  - Shows the secret word via underscores.
  - Prompts the user to type the guess.

![Main Screen](docs/screenshots/wwh-main-screen.png)

- __Correct Guess Screen__

  - If the player makes a correct letter guess, the letter is revealed
  - Feedback is provided to the user

![Correct Guess Screen](docs/screenshots/wwh-correct-guess.png)

- __Wrong Guess Screen__

  - If the player makes a wrong letter/word guess, a life is deducted from the player and feedback is provided.
  - The wrong letter can't be used by the player once again (meaning they won't lose another life if they try the same guess).

![Wrong Guess Screen](docs/screenshots/wwh-wrong-guess.png)

- __Invalid Guess Screen__

  - If the player attempts to input an invalid character (such as numbers or symbols), they will be thrown a message saying the guess was not valid.

![Invalid Guess Screen](docs/screenshots/wwh-invalid-guess.png)

- __Winning Game Screen__

  - If the player manages to guess the hidden word, they win the game!
  - The player is provided feedback and is prompted to play another round or not.

![Winning Game Screen](docs/screenshots/wwh-winning-screen.png)

- __Losing Game Screen__

  - If the player runs out of lives/tries before guessing the hidden word, they lose the game.
  - The player is provided feedback and is prompted to play another round or not.

![Losing Game Screen](docs/screenshots/wwh-game-over.png)

### Features Left to Implement

- High Score System
  - A high score system is a feature to keep in mind so the player can compete with friends/family.
- Choose difficulty
  - An option to give the player to choose an easier/medium/harder difficulty of the game.

## Technologies Used

### Language Used

- [Python3](https://developer.mozilla.org/en-US/docs/Glossary/Python)

### Frameworks, Libraries & Programs Used

- [Git](https://git-scm.com/) & [Gitpod](https://gitpod.io/)
  - Git was used for version control via the Gitpod terminal in order to commit to Git and push to GitHub.
- [GitHub](https://github.com/)
  - GitHub was used for version control.
- [Heroku](https://heroku.com/)
  - Heroku was used for hosting and deploying the game.

## Testing

### Validator Testing

- [PEP8online](http://pep8online.com/)
  - At first, four "E501" warnings (line too long) were returned when passing through the PEP8online check.

  ![PEP8online warning](docs/screenshots/wwh-pep8-warnings.png)

- [PEP8online](http://pep8online.com/)
  - The warning messages were addressed when I broke 3 of the 4 lines (making them shorter) with a backslash ("\").
  - The remaining line was addressed with a "#noqa" comment. After implementing these fixes the linter validated the code with no issues.

  ![PEP8online validation pass](docs/screenshots/wwh-pep8-validation-pass.png)

### Device Testing

- The Weird Word Hangman was tested on the following devices/environments (without any major issues):
  - MacBook Air 13.3" M1 (macOS Big Sur 11.6)
  - Lenovo 5i 15" i5 (Windows 10 64x)

### Browser Testing

### Features Testing

### Bugs

## Deployment

## Credits 

### Content

### Media

### Other