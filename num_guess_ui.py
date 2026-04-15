import tkinter as tk
import random
 
#Game Variables
number_to_guess = None
max_number = 100
attempts = 0
max_attempts = 3
score = 100

#Function to start new game

def start_game(level):
    global number_to_guess,max_number,attempts,score
    attempts = 0
    score = 100
    
    if level == 1:
        max_number = 50
    elif level == 2:
        max_number = 100
    elif level == 3:
        max_number = 500
    else:
        max_number = 100
    
    number_to_guess = random.randint(1,max_number)
    result_label.config(text=f"Guess a number between 1 and {max_number}")
    entry.delete(0,tk.END)

#Function to check guess
def check_guess():
    global attempts , score
    try:
        guess = int(entry.get())
        attempts+=1

        if guess == number_to_guess:
            result_label.config(text=f"Correct! Score : {score}")
        elif guess < number_to_guess:
            result_label.config(text=f"Too Low! Try again")
            score -=5
            entry.delete(0,tk.END)
        else:
            result_label.config(text=f"Too High! Try again")
            score -= 5
            entry.delete(0,tk.END)
            
        if attempts == max_attempts and guess != number_to_guess:
            result_label.config(text=f"Game over! Number was {number_to_guess}")
    except ValueError:
        result_label.config(text="Please enter a valid number!")
        
#Tkinter window setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.config(bg="#f0f0f0")

#Title Banner
title_label = tk.Label(root, text="🎮 Number Guessing Game 🎮", font=("Arial",16,"bold"),bg="#f0f0f0",fg="darkblue")
       
#Difficulty Buttons
tk.Label(root,text="Choose Difficulty:" ,font=("Arial", 12), bg="#f0f0f0").pack()
tk.Button(root, text="Easy (1-50)",command=lambda:start_game(1), bg="lightgreen", font=("Arial", 10)).pack()
tk.Button(root, text="Medium (1-100)",command=lambda:start_game(2), bg="lightyellow", font=("Arial", 10)).pack()
tk.Button(root, text="Hard (1-500)",command=lambda:start_game(3), bg="lightcoral", font=("Arial", 10)).pack()

#Input field
entry = tk.Entry(root,font=("Arial", 12), justify="center")
entry.pack(pady=10)

#Guess button
tk.Button(root, text="Guess",command=check_guess, bg="skyblue", font=("Arial", 12, "bold")).pack()

#Result label
result_label = tk.Label(root, text="",font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=20)


root.mainloop()