import tkinter as tk
from tkinter.messagebox import showinfo
import random

window = tk.Tk()
window.title("Iranian DoZe Game")

global turn, results, player_points
turn = "X"
results = ["", "", "", "", "", "", "", "", ""]
player_points = [0, 0]

def clicked(btn):
    global turn
    btn = int(btn)

    if results[btn] == "":
        if turn == "X":
            results[btn] = "X"
            buttons[btn]["bg"] = "red"
            buttons[btn]["fg"] = "white"
            buttons[btn]["text"] = "X"
            buttons[btn]["relief"] = tk.GROOVE
            turn = "O"
            choice = random.choice([i for i in range(9) if results[i] == ""])
            clicked(choice)
        else:
            results[btn] = "O"
            buttons[btn]["bg"] = "green"
            buttons[btn]["fg"] = "white"
            buttons[btn]["text"] = "O"
            turn = "X"
    rule()

def rule():
    if (results[0] == results[1] == results[2] and results[0] != ""):
        show_winner(results[0])
    elif (results[3] == results[4] == results[5] and results[3] != ""):
        show_winner(results[3])
    elif (results[6] == results[7] == results[8] and results[6] != ""):
        show_winner(results[6])
    elif (results[0] == results[3] == results[6] and results[0] != ""):
        show_winner(results[0])
    elif (results[1] == results[4] == results[7] and results[1] != ""):
        show_winner(results[1])
    elif (results[2] == results[5] == results[8] and results[2] != ""):
        show_winner(results[2])
    elif (results[0] == results[4] == results[8] and results[0] != ""):
        show_winner(results[0])
    elif (results[2] == results[4] == results[6] and results[2] != ""):
        show_winner(results[2])
    else:
        check_draw()

def show_winner(winner):
    if winner == "X":
        player_points[0] += 1
        showinfo("Finish the game", "Player #1 wins")
        reset()
    else:
        player_points[1] += 1
        showinfo("Finish the game", "The system won over you")
        reset()

def reset():
    global results, turn
    results = ["", "", "", "", "", "", "", "", ""]
    turn = "X"
    points()
    board()

def check_draw():
    if "" not in results:
        showinfo("Finish the game", "The game equalised")
        reset()

def points():
    board_frame = tk.Frame(window)
    board_frame.grid(row=0)
    label_player_one = tk.Label(board_frame, text="Player 1", font=("Aviny", 16), padx=10)
    label_player_two = tk.Label(board_frame, text="Player 2", font=("Aviny", 16), padx=10)
    label_player_one.grid(row=0, column=0)
    label_player_two.grid(row=0, column=2)

    point_frame = tk.Frame(window)
    point_frame.grid(row=1)
    point_player_one = tk.Label(point_frame, text=player_points[0], padx=20, font=("Lalezar", 18))
    point_player_two = tk.Label(point_frame, text=player_points[1], padx=20, font=("Lalezar", 18))
    point_player_one.grid(row=0, column=0)
    point_player_two.grid(row=0, column=1)

def board():
    global buttons
    buttons = []
    counter = 0
    board_frame = tk.Frame(window)
    board_frame.grid(row=2)
    for row in range(1, 4):
        for column in range(1, 4):
            index = counter
            buttons.append(index)
            buttons[index] = tk.Button(board_frame, command=lambda x=f"{index}": clicked(x))
            buttons[index].config(width=10, height=4, font=("None", 18, "bold"))
            buttons[index].grid(row=row, column=column)
            counter += 1

points()
board()

window.mainloop()