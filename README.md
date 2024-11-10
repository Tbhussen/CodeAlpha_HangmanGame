# CodeAlpha_HangmanGame
Created a Hangman game as part of Python Programming Internship with Code Alpha
## Detailed Discription
This program is a text-based Hangman game where players guess the name of an animal letter by letter. The game loads a random animal name from a provided file and gives the player up to six mistakes before ending. If the player correctly guesses the animal, they win; otherwise, the game displays a "Game Over" message after seven incorrect attempts.

### Requirements
Python 3.x

A text file containing animal names (one per line), which should be located at C:\Users\ji160\OneDrive\Desktop\CodeAlpha\animals.txt.

### Instructions
The program opens and reads an animal name from the animals.txt file, storing it in a list.

It selects a random animal from this list and asks the player to guess the animal's name one letter at a time.

The player has up to six incorrect guesses. With each mistake, the program visually displays a part of a "hangman" figure.

Correct guesses reveal the corresponding letters in the animal name.

The game ends either when:

1. The player correctly guesses all letters in the animal name, or

2. The player makes seven incorrect guesses, resulting in a "Game Over."

### Code Explanation
#### Main Variables:

data_into_list: Holds all animal names from the file.

animal: Randomly chosen animal name converted to lowercase.

blist: Boolean list where each element corresponds to a letter in the animal name, indicating if it has been guessed.

used_letters: List of letters the player has already guessed.

mistakes: Tracks the number of incorrect guesses.

#### Functions:
display(mistakes): Outputs the hangman graphic depending on the number of mistakes.

GameEndWinner(animal): Displays a winning message when the player successfully guesses the animal.

GameEndLoser(animal): Displays a "Game Over" message with the correct animal name.

show_current_status(blist, length, wlist): Shows the current state of the guessed animal name, with correctly guessed letters displayed.
