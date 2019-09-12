import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')

import Leap #why is there no module named Leap?

import constants
import pygameWindow

class DELIVERABLE:


    def __init__(self, x, y, xMin, xMax, yMin, yMax):
        self.controller = Leap.Controller()
        self.pygameWindow = pygameWindow.PYGAME_WINDOW()
        self.frame = self.controller.frame()
        self.x = x
        self.y = y
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax

    #copied Scale() over from Del01
    def Scale(self, coord, leapMin, leapMax, winMin, winMax):  # this Min could be zero dammit
        screenwidth = winMax - winMin
        scalar = 3
        ratio = (((scalar * coord) + ((leapMax - leapMin) / 2)) / (leapMax - leapMin))
        print(ratio)
        return int((ratio) * (screenwidth))

    def Handle_Vector_From_Leap(self, v):
        xPre = int(v[0])
        yPre = int(v[2])  # why not v[1]?
        # axis control (leapMin and leapMax)
        if xPre < self.xMin:
            xPre = self.xMin
        if xPre > self.xMax:
            xPre = self.xMax
        if yPre < self.yMin:
            yPre = self.yMin
        if yPre > self.yMax:
            yPre = self.yMax

    def Handle_Bone(self, bone):
        base = bone.prev_joint
        tip = bone.next_joint
        xBase, yBase = self.Handle_Vector_From_Leap(base)
        xTip, yTip = self.Handle_Vector_From_Leap(tip)
        pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, (3 - b))
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
        if len(handList) > 0:  # use isempty to track values of objects in the list
            #handList = self.frame.hands
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

                    self.Handle_Finger(finger)
