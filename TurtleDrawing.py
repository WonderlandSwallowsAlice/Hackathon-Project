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
