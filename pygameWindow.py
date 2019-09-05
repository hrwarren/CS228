import pygame
import constants

class PYGAME_WINDOW:
    #PYGAME_WINDOW class's constructor 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowDepth)) #note: 300,100 represents screen height and width

    def Prepare(self):
        pygame.event.get()
        self.screen.fill(constants.white) #makes window white
    
    def Reveal(self):  
        pygame.display.update()
    
    def Draw_Black_Circle(self,x,y): 
        pygame.draw.circle(self.screen, constants.black, [x,y], 20) #args are (screen, color, coordinates, size)

#SOLUTION TO NAMEERROR: don't use the @classmethod decorator! Problem solved


#EVERYTHING BELOW IS RESOLVED

#When everything is in its current state and I use self.screen.fill(...), get NameError: global name 'self' is not defined
#Running pygameWindow.py in terminal in its current state gives no errors

#Moving self.screen.fill(...) to def __init__(self) section removes the error, but makes the screen permanently white
#Removing self and making it screen.fill(...) just makes screen the undefined variable instead
#Removing pygame.event.get() does not change error
#Making Prepare(cls) into Prepare(self) instead; got AttributeError: class PYGAME_WINDOW has no attribute 'screen'
#Making self.screen........ into cls.screen...... yields the same AttributeError as above
#Changing anything about the indentation just yields IndentationError: unexpected indent
#Adding self as an argument to Prepare(cls) gets TypeError: Prepare() takes exactly 2 arguments (1 given)