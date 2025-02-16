
import turtle
import pygame
import pygame_menu
import threading

import pygame_menu.events

Height = 600
Width = 600
bgcolor = 'white'
ttcolor = 'black'

def start_the_game():
    # gather user inputs for height, width, background color, and turtle/line color
    #data = input("Please enter the height and width separated by a space: ").split()
    #Height = int(data[0])
    #Width = int(data[1])

    #bgcolor = input("Please enter the color of your background: ")

    #ttcolor = input("Please enter the color of your turtle: ")

    global Height, Width, bgcolor, ttcolor

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

    def make_circle():
        etch.circle(100)


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

def run_game():
    game_thread = threading.Thread(target=start_the_game)
    game_thread.start()

#menu for game
pygame.init()
surface = pygame.display.set_mode((600, 600))


#main menu
menu = pygame_menu.Menu('Welcome', 600, 600, theme=pygame_menu.themes.THEME_BLUE)

menu.add.label('Turtle Etch-A-Sketch')
menu.add.button('Play', start_the_game)
menu.add.button('Options', lambda: optionsMenu.mainloop(surface))
menu.add.button('Quit', pygame_menu.events.EXIT)

#options menu
optionsMenu = pygame_menu.Menu('Options', 600, 600, theme=pygame_menu.themes.THEME_BLUE)
optionsMenu.add.label('Options Menu')
optionsMenu.add.text_input('Height: ', default='600', onchange=lambda value: set_global('Height', value))
optionsMenu.add.text_input('Width: ', default='600', onchange=lambda value: set_global('Width', value))
optionsMenu.add.text_input('Background Color: ', default='white', onchange=lambda value: set_global('bgcolor', value))
optionsMenu.add.text_input('Turtle Color: ', default='black', onchange=lambda value: set_global('ttcolor', value))
#optionsMenu.add.button('Back', pygame_menu.events.BACK)
backButton = optionsMenu.add.button('Back', lambda: optionsMenu.disable())

def set_global(var_name, value):
    global Height, Width, bgcolor, ttcolor
    try:
        if var_name == 'Height':
            Height = max(int(value), 100)  
        elif var_name == 'Width':
            Width = max(int(value), 100) 
    except ValueError:
        if var_name == 'Height':
            Height = 600 
        elif var_name == 'Width':
            Width = 600  
    if var_name == 'bgcolor':
        bgcolor = value
    elif var_name == 'ttcolor':
        ttcolor = value

menu.mainloop(surface)
