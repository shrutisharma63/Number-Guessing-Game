import tkinter as tk
import random
 
#Game Variables
number_to_guess = None
max_number = 100
attempts = 0
max_attempts = 10
score = 100
last_level = 2
replay_button = None
high_score = 0 #for checking high score
time_left = 30 #default timer 30 seconds
game_over = False

#Function to start new game
def start_game(level):
    global number_to_guess,max_number,attempts,score,last_level,replay_button,time_left,game_over
    attempts = 0
    score = 100
    last_level = level
    time_left = 30#reset timer each game
    game_over = False
    
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
    #Hide Replay Button when game starts
    if replay_button is not None:
       replay_button.pack_forget() 
       replay_button = None
       
    #start timer
    start_timer()


#Countdown timer function
def start_timer():
    global time_left,attempts,max_attempts
    if attempts >= max_attempts:
        return
    if time_left > 0:
        timer_label.config(text=f"🕛Time Left: {time_left}")
        time_left -= 1
        root.after(1000,start_timer) #call again after 1 second
    else:
        timer_label.config(text=f"Time's Up! Number was {number_to_guess} | High score {high_score}")
        show_replay_button()
    
#Function to check guess
def check_guess():
    global attempts , score ,high_score
    try:
        guess = int(entry.get())
        attempts+=1

        if guess == number_to_guess:
            if score > high_score:
                high_score = score
            show_replay_button()
            result_label.config(text=f"🎉 Correct! NUmber : {number_to_guess} | 🏆 High Score: {high_score}")
        elif guess < number_to_guess:
            result_label.config(text=f"Too Low! Try again")
            score -=5
            entry.delete(0,tk.END)
        else:
            result_label.config(text=f"Too High! Try again")
            score -= 5
            entry.delete(0,tk.END)
            
        if attempts == max_attempts and guess != number_to_guess:
            if score > high_score:
                high_score = score
            result_label.config(text=f"Game over! Number was {number_to_guess} | High Score : {high_score}")
            show_replay_button()
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

#Function to show replay button
def show_replay_button():
    global replay_button
    if replay_button is None:
        replay_button = tk.Button(root, text="Replay", command=lambda: start_game(last_level),bg="lightpink", font=("Arial",12,"bold"))
        replay_button.pack(pady=5)

#Result label
result_label = tk.Label(root, text="",font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=20)

#Timer Label
timer_label = tk.Label(root, text="",font=("Arial",12), bg="#f0f0f0",fg="red")
timer_label.pack()


root.mainloop()