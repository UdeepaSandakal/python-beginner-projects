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
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinate = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinate.append([0, 0])
        
        for x, y in self.coordinate:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinate = [x, y]
        canvas.create_oval(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=FOOD_COLOR, tags="food") 

def next_turn(snake, food):
    x, y = snake.coordinate[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinate.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE,fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    #deleting the last parts of the snake
    del snake.coordinate[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]

    window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction        #old direction
    
    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction

    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

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

#adding contolls to the snake
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))

snake = Snake()
food = Food()

#calling next_turn function
next_turn(snake, food) 

window.mainloop()

