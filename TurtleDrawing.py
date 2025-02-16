import turtle

# gather user inputs for height, width, background color, and turtle/line color
data = input("Please enter the height and width separated by a space: ").split()
Height = int(data[0])
Width = int(data[1])

bgcolor = input("Please enter the color of your background: ")

ttcolor = input("Please enter the color of your turtle: ")

turnspeed = input("Please enter how many units you would like the turtle to turn at a time: ")

movespeed = input("Please enter how many units you would like the turtle to move at a time: ")

# Setup the screen
screen = turtle.Screen()
screen.title("Etch A Sketch")
screen.bgcolor(bgcolor)
screen.setup(width=600, height=600)

# Create the turtle
etch = turtle.Turtle()
etch.shape(ttcolor)
etch.speed(0)

# Functions to move the turtle
def move_forward():
    etch.forward(int(movespeed))

def move_backward():
    etch.backward(int(movespeed))

def turn_left():
    etch.left(int(turnspeed))

def turn_right():
    etch.right(int(turnspeed))

def clear_screen():
    etch.clear()

def make_circle():
    etch.circle(100)

def make_square():
    for _ in range(4):
        etch.forward(100)
        etch.right(90)

def make_hexagon():
    for _ in range(6):
        etch.forward(100)
        etch.right(60)
    

def make_star():
    for _ in range(5):
        etch.forward(100)
        etch.right(144)
    
    
def make_flower():
    for _ in range(12):
        etch.right(30)
        etch.forward(40)
        etch.left(120)
        etch.forward(40)
        etch.left(120)
        etch.forward(40)
        etch.left(120)
        etch.forward(40)

def make_SEL():
    etch.forward(60)
    etch.left(90)
    etch.forward(60)
    etch.left(90)
    etch.forward(60)
    etch.right(90)
    etch.forward(60)
    etch.right(90)
    etch.forward(60)
    etch.right(180)
    etch.forward(60)
    etch.left(90)
    etch.forward(60)
    etch.left(90)
    etch.forward(60)
    etch.right(90)
    etch.forward(60)
    etch.left(90)
    etch.forward(60)
    etch.left(90)
    etch.forward(120)
    etch.right(90)
    etch.forward(60)
    etch.right(180)
    etch.forward(60)
    etch.left(90)
    etch.forward(60)
    etch.left(90)
    etch.forward(60)
    etch.right(180)
    etch.forward(60)
    etch.left(90)
    etch.forward(60)
    etch.left(90)
    etch.forward(120+60)
    etch.right(180)
    etch.forward(60)
    etch.right(90)
    etch.forward(120)

# Keyboard bindings
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_screen, "c")
screen.onkey(draw_circle, "1")

# Keep the window open
turtle.done()
