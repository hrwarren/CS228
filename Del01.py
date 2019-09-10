import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')
import Leap
from Leap import Bone
import pygame
import constants

 
#Do the code in Del01, then move the objects/methods/functions into pygame
#Then make everything self-referencing

from pygameWindow import PYGAME_WINDOW

#import constants
#import random

#circle position and axes
x = 0
y = 0

#Creating an instance of the PYGAME_WINDOW class
pygameWindow = PYGAME_WINDOW()

controller = Leap.Controller()

runStatus = True #this is now a switch

def Handle_Frame_Init(): #This function works in Del01, but fails if I move it to pygameWindow
    global x
    global y

    handList = frame.hands
    if len(handList) > 0: #use isempty to track values of objects in the list
        handList = frame.hands
        for hand in handList:
            fingers = hand.fingers
            if not fingers.is_empty:
                for finger in fingers:  # plural means it's a list, which is a static list (can hold anything)
                    indexFingerList = fingers.finger_type(finger.TYPE_INDEX)
                    indexFinger = indexFingerList[0]
                    distalPhalanx = indexFinger.bone(Bone.TYPE_DISTAL)

                    # matching your finger's xy coordinates to the dot's position
                    tip = distalPhalanx.next_joint
                    x = int(tip[0])
                    y = int(tip[2]) #deliverable says y should be the second value in tip, so why are we using the third?


                    # axis control (leapMin and leapMax)
                    if x < constants.xMin:
                        xMin = x
                    if x > constants.xMax:
                        xMax = x
                    if y < constants.yMin:
                        yMin = y
                    if y > constants.yMax:
                        yMax = y



def Scale(coord, leapMin, leapMax, winMin, winMax): #this Min could be zero dammit
    screenwidth = winMax - winMin
    scalar = 2
    ratio = (((scalar*coord) + ((leapMax-leapMin)/2)) / (leapMax - leapMin))
    print(ratio)
    return int((ratio) * (screenwidth))


while runStatus:
    pygameWindow.Prepare() #wipe window to prepare for drawing

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runStatus = False     #no self because no class  <----haha same

    frame = controller.frame()

    Handle_Frame_Init()

    pygameX = Scale(x, constants.xMin, constants.xMax, 0, constants.pygameWindowWidth)
    pygameY = Scale(y, constants.yMin, constants.yMax, 0, constants.pygameWindowDepth)

    print(pygameX, pygameY)

    pygameWindow.Draw_Black_Circle(pygameX, pygameY)

    pygameWindow.Reveal() #show drawn material to the user

#Code for troubleshooting invalid frame error
#     if(controller.is_connected):
#         frame = controller.frame()
#         previous = controller.frame(1)
#         print(frame)


#IMPORT ERROR RESOLVED: moved all leap library files out of x64 and into main lib folder.
#Why did this work? I have no idea
