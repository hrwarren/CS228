import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')
import Leap
import pygame

#pygameWindow.init()
 

# from pygameWindow import PYGAME_WINDOW
#import constants
#import random

#circle position
#x = 400
#y = 400

#Creating an instance of the PYGAME_WINDOW class
#pygameWindow = PYGAME_WINDOW()

controller = Leap.Controller()

runStatus = True #this is now a switch


while runStatus:

#    pygameWindow.Prepare() #wipe window to prepare for drawing
    if(controller.is_connected):
        frame = controller.frame()
        previous = controller.frame(1)
        print(frame)
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runStatus = False     #no self because no class

    frame = controller.frame()

    
    #print(controller)
    #true if at least one hand detected, false otherwise




#    pygameWindow.Draw_Black_Circle(x,y)

#    def Perturb_Circle_Position():
#        global x, y
#        fourSidedDieRoll = random.randint(1,4)
#        if fourSidedDieRoll == 1:
#            x = (x - 1)
#        elif fourSidedDieRoll == 2:
#            x = (x + 1)
#        elif fourSidedDieRoll == 3:
#            y = (y - 1)
#        else:
#            y = (y + 1)
    
#    Perturb_Circle_Position()

#    pygameWindow.Reveal() #show drawn material to the user

#print(pygameWindow)


#IMPORT ERROR RESOLVED: moved all leap library files out of x64 and into main lib folder.
#Why did this work? I have no idea

#As written, I get ImportError: No module named LeapPython
#Adding the entire directory as a string gets ImportError: No module named Leap
#Adding the entire directory not as a string gets SyntaxError: unexpected character after line continuation character