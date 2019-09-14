import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')

import Leap #why is there no module named Leap?

import constants
from pygameWindow_Del03 import PYGAME_WINDOW_Del03

class DELIVERABLE:


    def __init__(self, x, y, xMin, xMax, yMin, yMax):
        self.controller = Leap.Controller()
        self.pygameWindow = PYGAME_WINDOW_Del03()
        self.frame = self.controller.frame()

        #Could just bring all of these variables over from constants.py?
        self.x = x
        self.y = y
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax

        #should these even be here?


    #copied Scale() over from Del01
    def Scale(self, coord, leapMin, leapMax, winMin, winMax):  # this Min could be zero dammit
        screenwidth = winMax - winMin
        scalar = 3
        ratio = (((scalar * coord) + ((leapMax - leapMin) / 2)) / (leapMax - leapMin))
        print(ratio)
        return int((ratio) * (screenwidth))

    def Handle_Vector_From_Leap(self, v):
        self.xPre = int(v[0])
        self.yPre = int(v[2])  # why not v[1]?
        # axis control (leapMin and leapMax)
        if self.xPre < self.xMin: #I feel like making all of this self-referencing is broken
            self.xPre = self.xMin
        if self.xPre > self.xMax:
            self.xPre = self.xMax
        if self.yPre < self.yMin:
            self.yPre = self.yMin
        if self.yPre > self.yMax:
            self.yPre = self.yMax
        xv = self.Scale(self.xPre, constants.xMin, constants.xMax, 0, constants.pygameWindowWidth)
        yv = self.Scale(self.yPre, constants.yMin, constants.yMax, 0, constants.pygameWindowDepth)
        return(xv, yv)


    def Handle_Bone(self, bone):
        base = bone.prev_joint
        tip = bone.next_joint
        xBase, yBase = self.Handle_Vector_From_Leap(base)
        xTip, yTip = self.Handle_Vector_From_Leap(tip)

        print(self.numberOfHands)
        if self.numberOfHands == 1:
            self.pygameWindow.Draw_Line(constants.green, xBase, yBase, xTip, yTip, (3 - b))
        elif self.numberOfHands == 2:
            self.pygameWindow.Draw_Line(constants.red, xBase, yBase, xTip, yTip, (3 - b))

        print(xBase, yBase)
        print(xTip, yTip)

    def Handle_Finger(self, finger):
        global b
        for b in range(0, 4):
            bone = finger.bone(b)
            self.Handle_Bone(bone)

        xv = self.Scale(self.xPre, self.xMin, self.xMax, 0, constants.pygameWindowWidth)
        yv = self.Scale(self.yPre, self.yMin, self.yMax, 0, constants.pygameWindowDepth)
        print('v', xv, yv)
        # if xv < 0:
        #      xv = 0
        # if xv > 1200:
        #      xv = 1200
        return (xv, yv)

    def Handle_Frame_Init(self):  # This function works in Del01, but fails if I move it to pygameWindow

        handList = self.frame.hands
        self.currentNumberOfHands = len(handList) #can I define a self.variable down here?
        if self.numberOfHands > 0:  # use isempty to track values of objects in the list
            for hand in handList:
                fingers = hand.fingers
                for finger in fingers:
                    self.Handle_Finger(finger)
            self.previousNumberOfHands = self.currentNumberOfHands

    def Run_Forever(self):
        runStatus = True  # this is now a switch

    # I'm supposed to put everything below here in its own method, but I don't see why that's necessary
        while runStatus:
            self.pygameWindow.Prepare()  # wipe window to prepare for drawing

            self.frame = self.controller.frame()

            self.Handle_Frame_Init()

            self.pygameWindow.Reveal()  # show drawn material to the user

