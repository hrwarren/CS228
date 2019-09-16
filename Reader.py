import numpy as np
import pickle
import os
import constants
from pygameWindow_Del03 import PYGAME_WINDOW_Del03

class READER:
    def __init__(self):
        self.pickle_in = 0
        self.gestureData = np.zeros((5, 4, 6), dtype = 'f')
        self.xBaseNotYetScaled = np.zeros((5,4,3), dtype = 'f')
        self.yBaseNotYetScaled = np.zeros((5,4,3), dtype = 'f')
        self.pygameWindow = PYGAME_WINDOW_Del03()

        self.xMin = -600
        self.xMax = 600
        self.yMin = -600
        self.yMax = 600

#   Scale copied in from Del02
    def Scale(self, coord, leapMin, leapMax, winMin, winMax):
        screenwidth = winMax - winMin
        drawwidth = leapMax - leapMin
        scalar = 2
        # ratio = ((coord - (leapMax - leapMin)) / (winMax - winMin))
        ratio = (scalar * ((((coord * screenwidth) + drawwidth) / (drawwidth)))) + screenwidth / 2
        return (int(ratio))

    def Get_User_Data_Length(self):
        path, dirs, files = next(os.walk('userData'))
        self.numGestures = len(files)
        return(self.numGestures)

    def Print_Gestures(self):
        self.Get_User_Data_Length()
        for k in range(0, self.numGestures):
            self.pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData\gesture{}.p'.format(k), 'rb')
            self.gestureData = pickle.load(self.pickle_in)
            print(self.gestureData)
            print('I did something')

    def Draw_Gesture(self, i):
        self.pickle_in = open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\userData\gesture{}.p'.format(i), 'rb')
        self.gestureData = pickle.load(self.pickle_in)
        for g in range(0,6):
            for i in range(0,5):
                for j in range(0,4):
                    currentBone = self.gestureData[i, j, g]
                    xBasePre = self.gestureData[i,j,0]
                    yBasePre = self.gestureData[i,j,1]
                    xTipPre = self.gestureData[i,j,3]
                    yTipPre = self.gestureData[i,j,5]

                    xBase = self.Scale(xBasePre, self.xMin, self.xMax, 0, constants.pygameWindowWidth)
                    yBase = self.Scale(yBasePre, self.yMin, self.yMax, 0, constants.pygameWindowWidth)
                    xTip = self.Scale(xTipPre, self.xMin, self.xMax, 0, constants.pygameWindowWidth)
                    yTip = self.Scale(yTipPre, self.yMin, self.yMax, 0, constants.pygameWindowWidth)

                    #y, constants.yMin, constants.yMax, 0, constants.pygameWindowDepth

                    pygameWindow_Del03.Draw_Line()
                    print(i, xBase, yBase)
                    print(j, xTip, yTip)


                # self.gestureData[i, b, 0] = base[0]  # x
                # self.gestureData[i, b, 1] = base[1]  # y
                # self.gestureData[i, b, 2] = base[2]  # z

        self.pygameWindow.Prepare()
        #print(self.gestureData)
        self.pygameWindow.Reveal()
        #print(self.gestureData)
        print('I did something')

    def Draw_Each_Gesture_Once(self):
        self.Get_User_Data_Length()
        for i in range(0, self.numGestures):
            self.Draw_Gesture(i)


    def Draw_Gestures(self):
        runStatus = True  # this is now a switch
        # I'm supposed to put everything below here in its own method, but I don't see why that's necessary
        while runStatus:
            self.Draw_Each_Gesture_Once()
