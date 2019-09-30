import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')

import Leap #why is there no module named Leap?

import numpy as np

import pickle

import os
import shutil

import constants
from pygameWindow_Del03 import PYGAME_WINDOW_Del03

class RECORDER:


    def __init__(self, x, y, xMin, xMax, yMin, yMax):
        self.controller = Leap.Controller()
        self.pygameWindow = PYGAME_WINDOW_Del03()
        self.frame = self.controller.frame()
        self.currentNumberOfHands = 0
        self.previousNumberOfHands = 0
        self.numberOfGestures = 1000
        self.gestureData = np.zeros((5,4,6,self.numberOfGestures), dtype='f')
        self.gestureIndex = 0

        #Could just bring all of these variables over from constants.py?
        self.x = x
        self.y = y
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        #should these even be here?

        #3D matrix as a new variable:
        self.gestureNum = 0


    #copied Scale() over from Del02
    def Scale(self, coord, leapMin, leapMax, winMin, winMax):  # this Min could be zero dammit
        screenwidth = winMax - winMin
        drawwidth = leapMax - leapMin
        scalar = 2
        # ratio = ((coord - (leapMax - leapMin)) / (winMax - winMin))
        ratio = (scalar * ((((coord * screenwidth) + drawwidth) / (drawwidth)))) + screenwidth / 2
        #print(ratio)
        return (int(ratio))

    #copied Scale() over from Del01
    # def Scale(self, coord, leapMin, leapMax, winMin, winMax):  # this Min could be zero dammit
    #     screenwidth = winMax - winMin
    #     scalar = 3
    #     coordScaled = (scalar * (coord - (leapMax-leapMin)) * screenwidth) / (leapMax - leapMin)
    #     return(int(coordScaled))
    #     #ratio = (((scalar * coord) + ((leapMax - leapMin) / 2)) / (leapMax - leapMin))
    #     #print(ratio)
    #     #return int((ratio) * (screenwidth))

    def Handle_Vector_From_Leap(self, v):
        self.xPre = int(v[0])
        self.zPre = int(v[1])
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
        zv = self.zPre

        return(xv, yv, zv) #include zv even though it isn't scaled?


    def Handle_Bone(self, bone,i,b):
       # make sure you're not taking scaled values!!!!
        base = bone.prev_joint
        tip = bone.next_joint
        xBase, yBase, zBase = self.Handle_Vector_From_Leap(base)
        xTip, yTip, zTip = self.Handle_Vector_From_Leap(tip)

        #print(self.currentNumberOfHands)
        if self.currentNumberOfHands == 1:
            self.pygameWindow.Draw_Line(constants.green, xBase, yBase, xTip, yTip, (3 - b))
        elif self.currentNumberOfHands == 2:
            self.pygameWindow.Draw_Line(constants.red, xBase, yBase, xTip, yTip, (3 - b))

        if self.Recording_Is_Ending:  #eventually use a low-pass filter based on velocity of the hand to determine when to capture?
            self.gestureData[i, b, 0, self.gestureIndex] = base[0]   #x
            self.gestureData[i, b, 1, self.gestureIndex] = base[1]   #y
            self.gestureData[i, b, 2, self.gestureIndex] = base[2]   #z, but y for our purposes
            self.gestureData[i, b, 3, self.gestureIndex] = tip[0]
            self.gestureData[i, b, 4, self.gestureIndex] = tip[1]
            self.gestureData[i, b, 5, self.gestureIndex] = tip[2]


                # i and j are changing in here, but not in the i for loop print(i,j)


    def Handle_Finger(self, finger,i):
       # global b

        for b in range(0, 4):
            bone = finger.bone(b)
            self.Handle_Bone(bone, i, b)

        xv = self.Scale(self.xPre, self.xMin, self.xMax, 0, constants.pygameWindowWidth)
        yv = self.Scale(self.yPre, self.yMin, self.yMax, 0, constants.pygameWindowDepth)
        #print('v', xv, yv)
        # if xv < 0:
        #      xv = 0
        # if xv > 1200:
        #      xv = 1200

        return (xv, yv)

    def Clear_User_Data(self):
        userDataDir = 'C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData'
        try:
            shutil.rmtree(userDataDir)
        except:
            print('Error while deleting directory')

        #Should I save this to a variable name somewhere?
        #Also, why does this only work if file explorer is closed???????
        os.mkdir('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData')


    def Save_Gesture(self):
        userDataDir = 'C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData\gtest5.dat' #formerly ....gesture{}.p).format(self.gestureNum)
        pickle_out = open(userDataDir, 'wb')
        pickle.dump(self.gestureData, pickle_out)
        pickle_out.close()
        print('I did something')
        print(self.gestureData[:, :, :, 1])
        exit()

    def Recording_Is_Ending(self):
        #self.Save_Gesture()
        #self.gestureNum = self.gestureNum + 1
        print('recording is ending')



    def Handle_Frame_Init(self):
        handList = self.frame.hands
        self.currentNumberOfHands = len(handList)

        if self.currentNumberOfHands > 0:  # use isempty to track values of objects in the list
            #print('current', self.currentNumberOfHands, 'prev', self.previousNumberOfHands)

            if (self.previousNumberOfHands == 2) & (self.currentNumberOfHands == 1):
                self.Recording_Is_Ending()

            for hand in handList:
                fingers = hand.fingers

                for finger in fingers:
                    self.Handle_Finger(finger)
            self.previousNumberOfHands = self.currentNumberOfHands


    def Handle_Frame_Init_Recording(self):

        handList = self.frame.hands
        primaryHandList = handList[0]
        primaryFingers = primaryHandList.fingers
        # print(primaryHandList)
        # print(primaryFingers)
        self.currentNumberOfHands = len(handList)
        if self.currentNumberOfHands > 0:  # use isempty to track values of objects in the list
        # print('current', self.currentNumberOfHands, 'prev', self.previousNumberOfHands)
            if (self.previousNumberOfHands == 2) & (self.currentNumberOfHands == 1):
                self.Recording_Is_Ending()
            for hand in handList:
                fingers = hand.fingers
                i = -1  # it was -1 before? If it's stupid and it works, it ain't stupid
                for finger in fingers:
                    self.Handle_Finger(finger,i)

            for finger in primaryFingers:
                i = i+1
                self.Handle_Finger(finger,i)
            self.previousNumberOfHands = self.currentNumberOfHands
        if self.currentNumberOfHands == 2:
            print('gesture' + str(self.gestureIndex) + ' stored')
            self.gestureIndex = self.gestureIndex + 1
            if self.gestureIndex == self.numberOfGestures:
                print(self.gestureData[:,:,:,0])
                print(self.gestureData[:,:,:99])
                self.Save_Gesture()
                exit(0)




            #If there were previously 2 hands over the device but now there is only 1, end recording

    def Run_Forever(self):
        runStatus = True  # this is now a switch

    # I'm supposed to put everything below here in its own method, but I don't see why that's necessary
        while runStatus:
            self.pygameWindow.Prepare()  # wipe window to prepare for drawing

            self.frame = self.controller.frame()

            self.Handle_Frame_Init_Recording() #originally self.Handle_Frame_Init()

            self.pygameWindow.Reveal()  # show drawn material to the user

