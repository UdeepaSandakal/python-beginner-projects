from tkinter import*
import random

GAME_WIDTH = 500
GAME_HEIGHT = 500
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "FF0000"
BACKGROUND_COLOR = "#000000"


class snake:
    pass

class food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_direction():
    pass

def game_over():
    pass

window = Tk()
window.title("keeSnake")
window.resizable(False, False)

score = 0
direction = 'down'

lable = Label(window, text="Score:{}".format(score), font=('consolas', 40))
lable.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.mainloop()

