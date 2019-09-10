import sys

sys.path.insert(0, '..')
sys.path.insert(1, '../x86')
import Leap
from Leap import Bone
import pygame
import constants

from pygameWindow import PYGAME_WINDOW

# circle position and axes
x = 0
y = 0


# Creating an instance of the PYGAME_WINDOW class
pygameWindow = PYGAME_WINDOW()

controller = Leap.Controller()

runStatus = True  # this is now a switch

def Handle_Finger(finger):
    global b
    for b in range(0, 4):
        bone = finger.bone(b)
        Handle_Bone(bone)

def Handle_Bone(bone):
    base = bone.prev_joint
    tip = bone.next_joint
    xBase, yBase = Handle_Vector_From_Leap(base)
    xTip, yTip = Handle_Vector_From_Leap(tip)
    pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, (3-b))
    print(xBase, yBase)
    print(xTip, yTip)

def Handle_Vector_From_Leap(v):
    xPre = int(v[0])
    yPre = int(v[2]) #why not v[1]?

    # axis control (leapMin and leapMax)
    if xPre < constants.xMin:
        xPre = constants.xMin
    if xPre > constants.xMax:
        xPre = constants.xMax
    if yPre < constants.yMin:
        yPre = constants.yMin
    if yPre > constants.yMax:
        yPre = constants.yMax
    xv = pygameWindow.Scale(xPre, constants.xMin, constants.xMax, 0, constants.pygameWindowWidth)
    yv = pygameWindow.Scale(yPre, constants.yMin, constants.yMax, 0, constants.pygameWindowDepth)
    return(xv, yv)


def Handle_Frame_Init():  # This function works in Del01, but fails if I move it to pygameWindow
    global x
    global y


    handList = frame.hands
    if len(handList) > 0:  # use isempty to track values of objects in the list
        handList = frame.hands
        for hand in handList:
            fingers = hand.fingers
            for finger in fingers:

                # I HAVE EVERYTHING BUT THE AXIS CONTROL
                # WHAT AM I DOING HERE THAT IS DIFFERENT FROM WHAT I'M DOING IN DEL 01???
                # axis control (leapMin and leapMax)
                # if x < constants.xMin:
                #     xMin = x
                # if x > constants.xMax:
                #     xMax = x
                # if y < constants.yMin:
                #     yMin = y
                # if y > constants.yMax:
                #     yMax = y

                Handle_Finger(finger)


while runStatus:
    pygameWindow.Prepare()  # wipe window to prepare for drawing

    frame = controller.frame()

    Handle_Frame_Init()

    # Why does Bongard want this function call to be in Handle_Bone() instead of out here?
    #pygameWindow.Draw_Black_Line(xBase, xTip, yBase, yTip)

    pygameWindow.Reveal()  # show drawn material to the user