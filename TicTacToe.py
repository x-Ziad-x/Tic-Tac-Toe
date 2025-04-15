from tkinter import *
import random

def next_turn(row, column):
  global player

  if buttons[row][column]['text'] == "" and check_winner() is False:
    
    if player == players[0]:
      buttons[row][column]['text'] = player

      if check_winner() is False:
        player = players[1]
        label.config(text=(players[1]+" Turn"))

      elif check_winner() is True:
        label.config(text=(players[0]+" Wins"))

      elif check_winner() == "Tie":
        label.config(text=("Tie!"))

    else:
      buttons[row][column]['text'] = player

      if check_winner() is False:
        player = players[0]
        label.config(text=(players[0]+" Turn"))

      elif check_winner() is True:
        label.config(text=(players[1]+" Wins"))

      elif check_winner() == "Tie":
        label.config(text=("Tie!"))

def check_winner():
  #Horizantal Check Condition
  for row in range(3):
    if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
      buttons[row][0].config(bg="green")
      buttons[row][1].config(bg="green")
      buttons[row][2].config(bg="green")
      return True

  #Vertical Check Condition
  for column in range(3):
    if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
      buttons[0][column].config(bg="green")
      buttons[1][column].config(bg="green")
      buttons[2][column].config(bg="green")
      return True

  #Left Diagonal Check Condition
  if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
    buttons[0][0].config(bg="green")
    buttons[1][1].config(bg="green")
    buttons[2][2].config(bg="green")
    return True

  #Right Diagonal Check Condition
  elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
    buttons[0][2].config(bg="green")
    buttons[1][1].config(bg="green")
    buttons[2][0].config(bg="green")
    return True
  
  #Tie Check Condition
  elif empty_spaces() is False:
    for row in range(3):
      for column in range(3):
        buttons[row][column].config(bg="#FFC900")
    return "Tie"
  else:
    return False

def empty_spaces():
  spaces = 9
  for row in range(3):
    for column in range(3):
      if buttons[row][column]['text'] != "":
        spaces -=1

  if spaces == 0:
    return False
  else:
    return True

def new_game():
  global player

  player = random.choice(players)
  label.config(text=player + " Turn")

  for row in range(3):
    for column in range(3):
      buttons[row][column].config(text="", bg="#3B3B3B")

window= Tk()
window.title("Tic-Tac-Toe By Ziad")
window.geometry("465x636")
window.resizable(False, False)
window.config(bg="#202020")
players = ["X", "O"]
player = random.choice(players)

buttons =[[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

label = Label(window, text=player+" Turn", font=('consolas', 40), fg="white", bg="#202020")
label.pack(side="top")

reset_button = Button(window, text="Restart", font=('consolas', 20), fg="white", bg="#202020", command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
  for column in range(3):
    buttons[row][column] = Button(frame, text="", font=('consolas', 40), fg="white", bg="#3B3B3B", activebackground="#3B3B3B",
                                  width=5, height=2, command=lambda row=row, column=column : next_turn(row, column))
    buttons[row][column].grid(row=row, column=column)

window.mainloop()