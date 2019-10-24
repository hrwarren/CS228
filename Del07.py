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
programState = 0

# handOverDevice = False
wrongPosition = True

# Creating a switch
runStatus = True

# Creating an instance of the PYGAME_WINDOW class
pygameWindow = PYGAME_WINDOW()

# Initializing Leap controller
controller = Leap.Controller()
frame = controller.frame()

# Loading in the classifier
clf = pickle.load(open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\classifier_0135679_gettingthere.p'))

# Creating a vector to store the 30 features from the Leap Motion data
testData = np.zeros((1,30), dtype='f')

# Seed the random number generator
random.seed()

# Initialize points earned
points = 0

# The vector of dictionary keys:
digitsAttempted = ['digit0attempted',
                   'digit1attempted',
                   'digit2attempted',
                   'digit3attempted',
                   'digit4attempted',
                   'digit5attempted',
                   'digit6attempted',
                   'digit7attempted',
                   'digit8attempted',
                   'digit9attempted']

# The empty vector of times things have been drawn
times = []


# Getting username and info
database = pickle.load(open('userData/database.p','rb'))
username = raw_input('Please enter your name: ')
if username not in database:
    database[username] = {'logins': 1,
                          digitsAttempted[0]: 0,
                          digitsAttempted[1]: 0,
                          digitsAttempted[2]: 0,
                          digitsAttempted[3]: 0,
                          digitsAttempted[4]: 0,
                          digitsAttempted[5]: 0,
                          digitsAttempted[6]: 0,
                          digitsAttempted[7]: 0,
                          digitsAttempted[8]: 0,
                          digitsAttempted[9]: 0, }
    print('welcome ' + username + '.')

else:
    database[username]['logins'] = database[username]['logins'] + 1

    print('welcome back ' + username + '. \n You have logged in {} times.'.format(database[username]['logins'] ))

pickle.dump(database,open('userData/database.p', 'wb'))

userRecord = database[username]

print userRecord


# I feel like I should be making a separate script for a class and shoving
# all of the following functions into it, but I don't have time for that
# so here I am
def Scale(coord, leapMin, leapMax, winMin, winMax):  # this Min could be zero dammit
    screenwidth = winMax - winMin
    drawwidth = leapMax - leapMin
    scalar = 1
    ratio = ((coord - leapMin)/drawwidth) * screenwidth * scalar
    return int(ratio)

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
        testData[0, k] = tip[0]
        testData[0, k + 1] = tip[1]
        testData[0, k + 2] = tip[2]
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
    xv = Scale(xPre, xMin, xMax, 0, (constants.pygameWindowWidth)/2)
    yv = Scale(yPre, yMin, yMax, 0, (constants.pygameWindowDepth)/2)
    zv = zPre

    # if xv < 0:
    #      xv = 0
    # if xv > 1200:
    #      xv = 1200
    return(xv, yv, zv) #zv?


def Handle_Frame_Init(frame):
    global x
    global y
    global testData
    global k
    global predictedClass

    handList = frame.hands
    if len(handList) > 0:
        handList = frame.hands
        k = 0
#        for hand in handList:
        fingers = handList[0].fingers
        for finger in fingers:
            Handle_Finger(finger)
        # print(testData)
        testData = CenterData(testData)
        time.sleep(0.02)
        predictedClass = int(clf.Predict(testData))
        time.sleep(0.05)
       # print(predictedClass)

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
    global programState

    pygameWindow.showInitialImage()

    if len(frame.hands) > 0: #I want to make this a boolean: handOverDevice == True
        programState = 1

def HandleState1():
    global programState
    global wrongPosition
    global numToSign

    wrongPosition = False

    print(testData[0,12], testData[0,13], testData[0,14])

    if len(frame.hands) == 0:
        programState = 0

    # Hardcoded; will fix later
    # Instructions to center hand along x axis
    if testData[0, 12] < -4:
        pygameWindow.showMoveLeftImage()
        wrongPosition = True
    elif testData[0,12] > 4:
        pygameWindow.showMoveRightImage()
        wrongPosition = True

    # Instructions to center hand along y axis
    elif testData[0, 13] < 4:
        pygameWindow.showMoveForwardImage()
        wrongPosition = True
    elif testData[0,13] > 15:
        pygameWindow.showMoveBackwardImage()
        wrongPosition = True

    if not wrongPosition:
        pygameWindow.showSuccessImage()
        pygameWindow.Reveal()
        time.sleep(0.5)
        pygameWindow.Prepare()

        numToSign = random.randint(0, 9)
        programState = 2


def HandleState2():
    global programState
    global points
    global times

    if len(frame.hands) == 0:
        # database[username][digitsAttempted[numToSign]]= database[username].get(digitsAttempted[numToSign]) + 1
        # pickle.dump(database, open('userData/database.p', 'wb'))

        for i in range(0, 10):
            # times = [times, '{}: '.format(i) + '{} \n'.format(userRecord[digitsAttempted[i]])]
            if numToSign == i:
                database[username][digitsAttempted[i]] = database[username].get(digitsAttempted[i]) + 1
                pickle.dump(database, open('userData/database.p', 'wb'))
                print database[username][digitsAttempted[i]]
        programState = 0

    # times = '0: {}\n'.format(userRecord[digitsAttempted[0]]) + '1: {}\n'.format(userRecord[digitsAttempted[1]]) + '2: {}\n'.format(userRecord[digitsAttempted[2]]) + '3: {}\n'.format(userRecord[digitsAttempted[3]]) + '4: {}\n'.format(userRecord[digitsAttempted[4]]) + '5: {}\n'.format(userRecord[digitsAttempted[5]]) + '6: {}\n'.format(userRecord[digitsAttempted[6]]) + '7: {}\n'.format(userRecord[digitsAttempted[7]]) +'8: {}\n'.format(userRecord[digitsAttempted[8]]) + '9: {}\n'.format(userRecord[digitsAttempted[9]])


    # Just shows the number of times that digit has been attempted
    times = str(userRecord[digitsAttempted[numToSign]])

    print times

    pygameWindow.showNumToSign(numToSign)
    pygameWindow.showTimesAttempted(times)


    print(predictedClass, points)

    if predictedClass == numToSign:
        points = points + 1
        time.sleep(0.5)
        if points == 10:
            print(points)
            for i in range(0, 10):
                if numToSign == i:
                    database[username][digitsAttempted[i]] = database[username].get(digitsAttempted[i]) + 1
                    print database[username][digitsAttempted[i]]
                    pickle.dump(database, open('userData/database.p', 'wb'))
            programState = 3

    else:
        points = 0

def HandleState3():
    global programState
    global numToSign

    print database[username]

    pygameWindow.showSuccessImage()
    pygameWindow.Reveal()
    time.sleep(1)
    pygameWindow.Prepare()

    if len(frame.hands) > 0:
        # If hand off-center in x direction
        if testData[0, 12] < -4:
            wrongPosition = True
        elif testData[0, 12] > 4:
            wrongPosition = True

        # If hand off-center in y direction
        elif testData[0, 13] < 4:
            wrongPosition = True
        elif testData[0, 13] > 15:
            wrongPosition = True
        else:
            wrongPosition = False

        if wrongPosition:
            programState = 1
        else:
            numToSign = random.randint(0, 9)
            programState = 2
    else:
        programState = 0





while runStatus:

    pygameWindow.Prepare()  # wipe window to prepare for drawing
    frame = controller.frame()

    Handle_Frame_Init(frame)

    if programState == 0:
        HandleState0()
    elif programState == 1:
        HandleState1()
    elif programState == 2:
        HandleState2()
    elif programState == 3:
        HandleState3()

    pygameWindow.Reveal()  # show drawn material to the user



    # # Instructions to center hand along z axis
    # elif testData[0, 14] < 90:
    #     pygameWindow.showMoveUpImage()
    #     wrongPosition = True
    # elif testData[0,14] > 190:
    #     pygameWindow.showMoveDownImage()
    #     wrongPosition = True
