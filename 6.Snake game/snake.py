from tkinter import*
import random

GAME_WIDTH = 500
GAME_HEIGHT = 500
SPEED = 50
SPACE_SIZE = 30
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    pass

class Food:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tags="food") 

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

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenmmheight()

#how much we gonna adjust the position of our window
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}")

snake = Snake()
food = Food()

window.mainloop()

