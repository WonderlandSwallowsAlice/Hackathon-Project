
import turtle

# gather user inputs for height, width, background color, and turtle/line color
data = input("Please enter the height and width separated by a space: ").split()
Height = int(data[0])
Width = int(data[1])

bgcolor = input("Please enter the color of your background: ")

ttcolor = input("Please enter the color of your turtle: ")



# Setup the screen
screen = turtle.Screen()
screen.title("Etch A Sketch")
screen.bgcolor(bgcolor)
screen.setup(width=Width, height=Height)

# Create the turtle
etch = turtle.Turtle()
etch.shape("turtle")
etch.color(ttcolor)
etch.speed(0)

# Functions to move the turtle
def move_forward():
    etch.forward(10)

def move_backward():
    etch.backward(10)

def turn_left():
    etch.left(10)

def turn_right():
    etch.right(10)

def clear_screen():
    etch.clear()

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
screen.onkey(make_square, "q")
screen.onkey(make_hexagon, "h")
screen.onkey(make_star, "s")
screen.onkey(make_flower, "f")
screen.onkey(make_SEL, "e")
screen.onkey(make_circle, "1")

# Keep the window open
turtle.done()
