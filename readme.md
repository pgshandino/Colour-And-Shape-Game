# Color and Shape Guessing Game

This is a simple game that prompts the user to guess a randomly selected color or shape. The game provides visual feedback to the user to indicate whether their guess is correct or incorrect.

## Installation and Usage

1. Clone or download the repository.
2. Install the required packages: `pygame` and `tkinter`.
3. Run the game by executing the `main.py` file.

## How to Play

The game consists of two tabs - one for colors and the other for shapes. In each tab, the game provides a prompt to the user to select the correct color or shape.

## Color Game

In the __Colors__ tab, the game prompts the user to select a color that matches the randomly selected color from a list of colors. The game provides visual feedback to the user to indicate whether their guess is correct or incorrect.

## Shape Game

In the __Shapes__ tab, the game prompts the user to select a shape that matches the randomly selected shape from a list of shapes. The game provides visual feedback to the user to indicate whether their guess is correct or incorrect.

## Documentation

`play(guess, correct)`

This function plays a sound to provide feedback to the user based on their guess.

. `guess` (str): The user's guess.
. `correct` (str): The correct answer.

`ColorGame(master)`

This class represents the color guessing game.

. `master`: The root window.

Methods

`check_guess(guess)`: This method checks whether the user's guess is correct or not and provides visual feedback.

`ShapeGame(master)`

This class represents the shape guessing game.

`master`: The root window.

Methods

. `check_guess(guess)`: This method checks whether the user's guess is correct or not and provides visual feedback.

## Dependencies

The game requires the following packages:

1. pygame
2. tkinter
3. ttk

## Credits

This game was created by [Shanding]('https://www.linkedin.com/in/pgshanding')
