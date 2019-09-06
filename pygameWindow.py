import pygame
import constants
import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')
import Leap #still not able to import Leap for some reason???

class PYGAME_WINDOW:
    #PYGAME_WINDOW class's constructor 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowDepth)) #note: 300,100 represents screen height and width
        self.controller = Leap.Controller()
        self.frame = self.controller.frame()

    def Prepare(self):
        pygame.event.get()
        self.screen.fill(constants.white) #makes window white
    
    def Reveal(self):  
        pygame.display.update()
    
    def Draw_Black_Circle(self, x, y):
        # axis control (leapMin and leapMax)
        if x < 0:
            x = 0
        if x > constants.pygameWindowWidth:
            x = constants.pygameWindowWidth
        if y < 0:
            y = 0
        if y > constants.pygameWindowDepth:
            y = constants.pygameWindowDepth
        pygame.draw.circle(self.screen, constants.black, [x,y], 20) #args are (screen, color, coordinates, size)


    # def Handle_Frame_Init(self):
    #     handList = self.frame.hands
    #     print(len(handList))
    #     if len(handList) > 0:
    #         print('test')
    #         handList = self.frame.hands
    #         print('test')
    #         for hand in handList:
    #             print(hand)
    #             fingers = hand.fingers
    #             if not fingers.is_empty:
    #                 for finger in fingers: #plural means it's a list, which is a static list (can hold anything)
    #                     print('test')
    #                     indexFingerList = fingers.finger_type(finger.TYPE_INDEX)
    #                     indexFinger = indexFingerList[0]
    #                     distalPhalanx = indexFinger.bone(finger.bone.TYPE_DISTAL)
    #                     #print(distalPhalanx)
    #                     print(finger)
    #                     print(self.frame)



    #def Handle_Frame_Update(self, frame):

        #print(hand)



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