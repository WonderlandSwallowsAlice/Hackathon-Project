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
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Create the turtle
etch = turtle.Turtle()
etch.shape("turtle")
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

# Keyboard bindings
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_screen, "c")

# Keep the window open
turtle.done()
