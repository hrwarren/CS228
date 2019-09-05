from pygameWindow import PYGAME_WINDOW
import constants
import random

#circle position
x = 40
y = 400

#Creating an instance of the PYGAME_WINDOW class
pygameWindow = PYGAME_WINDOW()

while True:
    pygameWindow.Prepare() #wipe window to prepare for drawing
    
    pygameWindow.Draw_Black_Circle(x,y)

    def Perturb_Circle_Position():
        global x, y
        fourSidedDieRoll = random.randint(1,4)
        if fourSidedDieRoll == 1:
            x = (x - 1)
        elif fourSidedDieRoll == 2:
            x = (x + 1)
        elif fourSidedDieRoll == 3:
            y = (y - 1)
        else:
            y = (y + 1)
    
    Perturb_Circle_Position()

    pygameWindow.Reveal() #show drawn material to the user

print(pygameWindow)