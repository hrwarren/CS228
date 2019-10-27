import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')

import Leap
import constants
import pickle
import numpy as np
import time

from pygameWindow import PYGAME_WINDOW

class FRAME_HANDLER:

    def __init__(self):
        # self.controller = Leap.Controller()
        self.pygameWindow = PYGAME_WINDOW()
        # self.frame = self.controller.frame()

        self.clf = pickle.load(open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\classifier_0135679_gettingthere.p'))
        self.testData = np.zeros((1,30), dtype='f')
        self.k = 0

    def CenterData(self, data):
        for s in range(0, 2):
            allCoords = data[0, s::3]
            meanVal = allCoords.mean()
            data[0, s::3] = allCoords - meanVal
        return data


    def Scale(self, coord, leapMin, leapMax, winMin, winMax):   # Tested in Del6/Del02 - successful
        screenWidth = winMax - winMin
        drawWidth = leapMax - leapMin
        scalar = 1
        ratio = ((coord - leapMin) / drawWidth) * screenWidth * scalar
        return int(ratio)

    def Handle_Vector_From_Leap(self, v):   # Tested in Del07 - successful
        xPre = int(v[0])
        yPre = int(v[2])
        zPre = int(v[1])

        xv = self.Scale(xPre, constants.xMin, constants.xMax, 0, (constants.pygameWindowWidth) / 2)
        yv = self.Scale(yPre, constants.yMin, constants.yMax, 0, (constants.pygameWindowDepth) / 2)
        zv = zPre

        return xv, yv, zv

    def Handle_Finger(self,finger):
        global b
        for b in range(0, 4):
            bone = finger.bone(b)
            self.Handle_Bone(bone)

    def Handle_Bone(self,bone):
        #global k
        base = bone.prev_joint
        tip = bone.next_joint
        xBase, yBase, zBase = self.Handle_Vector_From_Leap(base)
        xTip, yTip, zTip = self.Handle_Vector_From_Leap(tip)
        if ((b == 0) or (b == 3)):
            self.testData[0, self.k] = tip[0]
            self.testData[0, self.k + 1] = tip[1]
            self.testData[0, self.k + 2] = tip[2]
            self.k = self.k + 3

        self.pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, (3 - b))
        print self.testData
        return self.testData


    def Handle_Frame_Init(self,frame):
        global x
        global y
        #global k

        handList = frame.hands
        if len(handList) > 0:
            handList = frame.hands
            self.k = 0
            #        for hand in handList:
            fingers = handList[0].fingers
            for finger in fingers:
                self.Handle_Finger(finger)
            # print(testData)
            self.testData = self.CenterData(self.testData)
            time.sleep(0.02)
            self.predictedClass = int(self.clf.Predict(self.testData))
            time.sleep(0.05)