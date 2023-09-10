import tkinter as tk
from tkinter import ttk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice and update the game
def play_game():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)

# Function to reset the game
def reset_game():
    user_choice_var.set("rock")
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Create labels for user and computer choices
user_choice_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
user_choice_label.grid(row=0, column=0, columnspan=2)

user_choice_var = tk.StringVar()
user_choice_var.set("rock")
user_choice_dropdown = ttk.Combobox(root, textvariable=user_choice_var, values=["rock", "paper", "scissors"])
user_choice_dropdown.grid(row=0, column=2)

# Create buttons to play and reset the game
play_button = ttk.Button(root, text="Play", command=play_game)
play_button.grid(row=1, column=0, columnspan=3)

reset_button = ttk.Button(root, text="Reset", command=reset_game)
reset_button.grid(row=2, column=0, columnspan=3)

# Create a label for game result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3)

# Start the GUI main loop
root.mainloop()
