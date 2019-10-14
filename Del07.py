import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')

import Leap
import constants
import pickle
import numpy as np
import random
import time

from pygameWindow import PYGAME_WINDOW


# Some nice global variables
x = 0
y = 0

xMin = constants.xMin
yMin = constants.yMin
xMax = constants.xMax
yMax = constants.yMax

# Turning this into a stateful program
# But not a stately program. It has no hope of that; it is a disaster
programState = 0
handOverDevice = False

# Creating a switch
runStatus = True

# Creating an instance of the PYGAME_WINDOW class
pygameWindow = PYGAME_WINDOW()

# Initializing Leap controller
controller = Leap.Controller()
frame = controller.frame()

# Loading in the classifier
clf = pickle.load(open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\classifier_30sets_low3.p', 'rb'))

# Creating a vector to store the 30 features from the Leap Motion data
testData = np.zeros((1,30), dtype='f')

# Seed the random number generator
random.seed()


# I feel like I should be making a separate script for a class and shoving
# all of the following functions into it, but I don't have time for that
# so here I am
def Scale(coord, leapMin, leapMax, winMin, winMax):  # this Min could be zero dammit
    screenwidth = winMax - winMin
    drawwidth = leapMax - leapMin
    scalar = 1
    ratio = ((coord - leapMin)/drawwidth) * screenwidth * scalar
    #ratio = (scalar * ((((coord * screenwidth) + drawwidth) / (drawwidth)))) + screenwidth/2
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
    #if the middle finger metacarpal tip (1,1,1) is out of a certain range
    #tell user to get back in
    pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, (3-b))

    # tell user to correct x coordinates


def Handle_Vector_From_Leap(v):
    global xMin
    global xMax
    global yMin
    global yMax

    xPre = int(v[0])
    yPre = int(v[2]) # why not v[1]?
    zPre = int(v[1])

    # originally pygameWindow.Scale
    xv = Scale(xPre, xMin, xMax, 0, (constants.pygameWindowWidth)/2)
    yv = Scale(yPre, yMin, yMax, 0, (constants.pygameWindowDepth)/2)
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
    global HandOverDevice
    global predictedClass

    handList = frame.hands

    if len(handList) > 0:  # or use isempty to track values of objects in the list
        HandOverDevice = True
        handList = frame.hands
        k = 0
        for hand in handList:
            fingers = hand.fingers
            for finger in fingers:
                Handle_Finger(finger)
        # print(testData)
            testData = CenterData(testData)
            time.sleep(0.02)
            predictedClass = clf.Predict(testData)
            #print(predictedClass)

def CenterData(testData):
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



def HandleState0():
    #global programState
    pygameWindow.showInitialImage()

    if len(frame.hands) > 0: #I want to make this a boolean: handOverDevice == True
        programState = 1

def HandleState1():
    #global programState
    global wrongPosition

    Handle_Frame_Init()
    wrongPosition = False


    #For some reason, the leap isn't being consistent on its coordinates
    #Am I using the wrong item in the testData vector?
    #print(testData[0,14])

    print(testData[0,11:14])

    # Instructions to center hand along x axis
    if testData[0, 12] < -2.6:
        pygameWindow.showMoveLeftImage()
        wrongPosition = True
    elif testData[0,12] > 0.2:
        pygameWindow.showMoveRightImage()
        wrongPosition = True

    # Instructions to center hand along y axis
    if testData[0, 13] < 4:
        pygameWindow.showMoveForwardImage()
        wrongPosition = True
    elif testData[0,13] > 7.1:
        pygameWindow.showMoveBackwardImage()
        wrongPosition = True

    # Instructions to center hand along z axis
    if testData[0, 14] < 90:
        pygameWindow.showMoveUpImage()
        wrongPosition = True
    elif testData[0,14] > 180:
        pygameWindow.showMoveDownImage()
        wrongPosition = True

    if not wrongPosition:
        # timer = 0
        # pygameWindow.pygame.time.get_ticks() + 2000
        #
        # if timer >= 2:
        #     pygameWindow.showSuccessImage()

        pygameWindow.showSuccessImage()
        # start = time.time()
        # elapsed = 0
        # while elapsed <= 3:
        #     elapsed = time.time()-start
        #     #I can't get the success image to stay put for longer than an instant
        # if elapsed >= 3:
        #     elapsed = time.time()-start
        #     time.sleep(0.5)
        #     pygameWindow.showSuccessImage()
        #     time.sleep(0.5)

        programState = 2

        print(wrongPosition)
        print(programState)

    if len(frame.hands) == 0:
        programState = 0

def HandleState2():
    global numToSign

    notDone = True
    numToSign = random.randint(0, 9)
    pygameWindow.showNumToSign(numToSign)

    Handle_Frame_Init()

    while notDone:
        for points in range(0, 10):
            if predictedClass == numToSign:
                points = points + 1
            else:
                points = 0
        if points == 10:
            notDone = False

    programState = 3





def HandleState3():
    pygameWindow.showSuccessImage()
    #pause at the reveal to show the success image

    if len(frame.Hands) > 0:
        if wrongPosition == False:
            programState = 2
        else:
            programState = 1
    else:
        programstate = 0







while runStatus:

    pygameWindow.Prepare()  # wipe window to prepare for drawing
    frame = controller.frame()

    if programState == 0:
        HandleState0()
    elif programState == 1:
        HandleState1()
    elif programState == 2:
        HandleState2()
    elif programState == 3:
        HandleState3()

    pygameWindow.Reveal()  # show drawn material to the user

    if programState == 3:   # pause after reveal to show success image
        time.sleep(1)
