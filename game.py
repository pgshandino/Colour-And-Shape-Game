import random
import tkinter as tk
from tkinter import ttk
import pygame

# Initialise the pygame mixer for playing sound effects
pygame.mixer.init()

def play(guess, correct):
    """
    Play a sound effect based on whether the guess is correct or not.

    Args:
    guess (str): The user's guess.
    correct (str): The correct answer.

    Returns:
    None
    """
    if guess == correct:
        # Load and play applause sound effect
        pygame.mixer.music.load("data/sounds/applause-cheering.mp3")
        pygame.mixer.music.play(loops=0)
    else:
        # Load and play fail sound effect
        pygame.mixer.music.load("data/sounds/soundfail-trombone-02.wav")
        pygame.mixer.music.play(loops=0)

class ColorGame:
    """
    A game where the user has to select the correct color from a list of options.
    """
    def __init__(self, master):
        self.master = master

        # Define a list of colors
        self.colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]

        # Choose a random color from the list
        self.correct_color = random.choice(self.colors)

        # Create a label to display the instruction
        self.label = tk.Label(self.master, text=f"Choose the colour {self.correct_color} from the options")
        self.label.pack()

        # Create buttons for each color
        self.buttons = []
        for color in self.colors:
            # Create a button with the color as its background and bind it to check_guess() and play()
            button = tk.Button(self.master, bg=color, width=10, height=5, command=lambda c=color: [self.check_guess(c), play(c, self.correct_color)])
            button.pack(side="left", padx=5)
            self.buttons.append(button)

    def check_guess(self, guess):
        """
        Check whether the user's guess is correct and display a feedback message.

        Args:
        guess (str): The user's guess.

        Returns:
        None
        """
        if guess == self.correct_color:
            message = "Correct!"
        else:
            message = "Incorrect. Try again."

        # Display the feedback message as a popup
        popup = tk.Toplevel(self.master)
        popup.title("Feedback")
        feedback_label = tk.Label(popup, text=message)
        feedback_label.pack()

class ShapeGame:
    def __init__(self, master):
        self.master = master

        # Define a list of shapes
        self.shapes = ["circle", "square", "triangle", "diamond", "star", "heart"]
        self.photos = {
                'circle': tk.PhotoImage(file="data/images/Circle.png"),
                'square': tk.PhotoImage(file="data/images/Square.png"),
                'triangle': tk.PhotoImage(file="data/images/Triangle.png"),
                'diamond': tk.PhotoImage(file="data/images/Diamond.png"),
                'star': tk.PhotoImage(file="data/images/Star.png"),
                'heart': tk.PhotoImage(file="data/images/Heart.png"),
            }

        # Choose a random shape from the list
        self.correct_shape = random.choice(self.shapes)

        # Create a label to display the instruction
        self.label = tk.Label(self.master, text=f"Select the {self.correct_shape} shape from the options")
        self.label.pack()

        # Create buttons for each shape
        self.buttons = []
        for shape in self.shapes:
            button = tk.Button(self.master, text=shape, image=self.photos[shape], width=100, height=100, command=lambda c=shape: [self.check_guess(c), play(c, self.correct_shape)])
            button.pack(side="left", padx=5)
            self.buttons.append(button)

    def check_guess(self, guess):
        # Check if the guess is correct
        if guess == self.correct_shape:
            message = "Correct!"
        else:
            message = "Incorrect. Try again."

        # Display the feedback message as a popup
        popup = tk.Toplevel(self.master)
        popup.title("Feedback")
        feedback_label = tk.Label(popup, text=message)
        feedback_label.pack()

# Create the main window
root = tk.Tk()
root.title("Color and Shape Guessing Game")

# Create two tabs - one for colors and the other for shapes
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Colors")
tab_control.add(tab2, text="Shapes")
tab_control.pack(expand=1, fill="both")

# Start the color and shape games in their respective tabs
color_game = ColorGame(tab1)
shape_game = ShapeGame(tab2)

root.mainloop()
