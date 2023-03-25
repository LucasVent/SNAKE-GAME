# SNAKE GAME !!!

from tkinter import *
import random 


GAME_WIDTH = 700
GAME_HEIGTH = 700
SPEED = 50
SPACE_SIZE = 50
BOOD_PARTS = 3
SNAKE_COLOR = "#09FF00"
FOOD_COLOR = "#DB1414"
BACKGROUND_COLOR = "#000000"



class Snake():
    
    def __init__(self):

        self.body_size = BOOD_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BOOD_PARTS):
            self.coordinates.append([0, 0])


        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="Snake")
            self.squares.append(square)

class Food():

    def __init__(self):


        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGTH / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]


        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")



def Next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    
    snake.coordinates.insert(0,(x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    del snake.coordinates[-1]

    canvas.delete(snake.squares[-1])

    del snake.squares[-1]

    

    window.after(SPEED, Next_turn, snake, food)



def Change_direction(new_direction):

    global direction

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


def Check_collisions():
    pass

def Game_over():
    pass


window = Tk()
window.title("Snake game")
window.resizable(False,False)
score = 0
direction = 'down'

label = Label(window, text="score:{}".format(score), font=('consolas', 40))
label.pack()
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGTH, width=GAME_WIDTH )
canvas.pack()

window.update()
window_width = window.winfo_width()
window_heigth = window.winfo_height()
screem_width = window.winfo_screenwidth()
screem_heigth = window.winfo_screenheight()

x = int((screem_width/2) - (window_width/2))
y = int((screem_heigth/2) - (window_heigth/2))

window.geometry(f"{window_width}x{window_heigth}+{x}+{y}")

window.bind('<left>', lambda event: Change_direction('left'))
window.bind('<right>', lambda event: Change_direction('right'))
window.bind('<up>', lambda event: Change_direction('up'))
window.bind('<down>', lambda event: Change_direction('down'))



snake = Snake()
food = Food()

Next_turn(snake, food)

window.mainloop()



mudar_direcao = [

    {'left': 'right'}


]