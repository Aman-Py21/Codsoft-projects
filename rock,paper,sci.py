import tkinter as tk
from tkinter import messagebox
import random

# Game logic
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score, rounds_played  # Declare as global
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        user_score += 1
        rounds_played += 1
        return "You win!"
    else:
        computer_score += 1
        rounds_played += 1
        return "Computer wins!"

def play_game(user_choice):
    global rounds_played  # Declare as global
    if rounds_played >= 5:
        if user_score >= 3:
            messagebox.showinfo("Game Over", "You won the game!")
        elif computer_score >= 3:
            messagebox.showinfo("Game Over", "Computer won the game!")
        else:
            messagebox.showinfo("Game Over", "It's a tie game!")
        reset_game()
        return

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    # Update the result and score
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}\nRounds Played: {rounds_played}")

def reset_game():
    global user_score, computer_score, rounds_played  # Declare as global
    user_score = 0
    computer_score = 0
    rounds_played = 0
    result_label.config(text="Make your choice to start!")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}\nRounds Played: {rounds_played}")

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x450")
root.resizable(False, False)

# Variables for score tracking
user_score = 0
computer_score = 0
rounds_played = 0

# Title Label
title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Instructions
instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors to play.", font=("Arial", 12))
instructions_label.pack(pady=5)

# Result Display
result_label = tk.Label(root, text="Make your choice to start!", font=("Arial", 12), fg="blue", justify="center")
result_label.pack(pady=10)

# Buttons for User Choices
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 14), bg="#f44336", fg="white", width=10, command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 14), bg="#2196f3", fg="white", width=10, command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 14), bg="#4caf50", fg="white", width=10, command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Score Display
score_label = tk.Label(root, text=f"Your Score: {user_score} | Computer Score: {computer_score}\nRounds Played: {rounds_played}", font=("Arial", 12), fg="black")
score_label.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), bg="#ffc107", fg="black", command=reset_game)
reset_button.pack(pady=20)

# Run the application
root.mainloop()
