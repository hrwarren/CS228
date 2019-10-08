import sys

sys.path.insert(0, '../..')
sys.path.insert(1, '../../x86')

import Leap
import constants
import pickle
import numpy as np

from pygameWindow import PYGAME_WINDOW

# This whole thing might go to shit as soon as I plug in the Leap Motion
# Just a heads up

# Some nice global variables
x = 0
y = 0

xMin = constants.xMin
yMin = constants.yMin
xMax = constants.xMax
yMax = constants.yMax

# Creating a switch
runStatus = True

# Creating an instance of the PYGAME_WINDOW class
pygameWindow = PYGAME_WINDOW()

# Initializing Leap controller
controller = Leap.Controller()
frame = controller.frame()

# Loading in the classifier
clf = pickle.load(open('userData/classifier101.p', 'rb'))

# Creating a vector to store the 30 features from the Leap Motion data

testData = np.zeros((1,30), dtype='f')


# I feel like I should be making a separate script for a class and shoving
# all of the following functions into it, but I don't have time for that
# so here I am
def Scale(coord, leapMin, leapMax, winMin, winMax):  # this Min could be zero dammit
    screenwidth = winMax - winMin
    drawwidth = leapMax - leapMin
    scalar = 2
    ratio = (scalar * ((((coord * screenwidth) + drawwidth) / (drawwidth)))) + screenwidth/2
    return (int(ratio))

def Handle_Finger(finger):
    global b
    for b in range(0, 4):
        bone = finger.bone(b)
        Handle_Bone(bone)

def Handle_Bone(bone):
    global k
    base = bone.prev_joint
    tip = bone.next_joint
    xBase, yBase, zBase = Handle_Vector_From_Leap(base)
    xTip, yTip, zTip = Handle_Vector_From_Leap(tip)
    if ((b == 0) or (b == 3)):
        if (k < 30):
            testData[0, k] = xTip
            testData[0, k + 1] = yTip
            testData[0, k + 2] = zTip
            k = k + 3

    pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, (3-b))

def Handle_Vector_From_Leap(v):
    global xMin
    global xMax
    global yMin
    global yMax

    xPre = int(v[0])
    yPre = int(v[2]) # why not v[1]?
    zPre = int(v[1])

    # originally pygameWindow.Scale
    xv = Scale(xPre, xMin, xMax, 0, constants.pygameWindowWidth)
    yv = Scale(yPre, yMin, yMax, 0, constants.pygameWindowDepth)
    zv = zPre

    # if xv < 0:
    #      xv = 0
    # if xv > 1200:
    #      xv = 1200
    return(xv, yv, zv) #zv?


def Handle_Frame_Init():  # This function works in Del01, but fails if I move it to pygameWindow
    global x
    global y
    global testData
    global k

    handList = frame.hands
    if len(handList) > 0:  # or use isempty to track values of objects in the list
        handList = frame.hands
        k = 0
        for hand in handList:
            fingers = hand.fingers
            for finger in fingers:
                Handle_Finger(finger)
        # print(testData)
            testData = CenterData(testData)
            predictedClass = clf.Predict(testData)
            print(predictedClass)

def CenterData(vec):
    for s in range(0,2):
        allCoords = testData[0,s::3]
        meanVal = allCoords.mean()
        testData[0, s::3] = allCoords - meanVal
    return testData

# def CenterData(X):
#     for s in range(0,3):
#         allXCoords = X[:,:,s,:]
#         meanValue = allXCoords.mean()
#         X[:,:,s,:] = allXCoords - meanValue
#     return X


while runStatus:
    pygameWindow.Prepare()  # wipe window to prepare for drawing

    frame = controller.frame()

    Handle_Frame_Init()

    # pygameWindow.Draw_Black_Line(xBase, xTip, yBase, yTip)

    pygameWindow.Reveal()  # show drawn material to the user