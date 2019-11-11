import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')

import Leap
import constants
import pickle
import numpy as np
import random
import time
import operator

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
clf = pickle.load(open('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData\classifier_0123456789_k100.p'))

# Creating a vector to store the 30 features from the Leap Motion data
testData = np.zeros((1,30), dtype='f')

# Seed the random number generator
random.seed()
randNum = 0

# Initialize points earned
points = 0

# Initialize the counter that determines if digits have been attempted
start = 0

# Initialize counter of how many times failed
fail = 0

# Init counter of how many seconds have passed since image shown
sec = 0

prevtime = time.time()

# Number of times user must succeed on a number to proceed
thresh = 4
achieved = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Initialize the dictionary for storing the leaderboard
leaderboard = {}

# divisor for scaling drawing window
divisor = 2
# 2 to take up 1/4 of the window
# 1 to take up all of the window

# run score for the speedrun mode
runScore = 0

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

digitsSucceeded = ['digit0succeeded',
                   'digit1succeeded',
                   'digit2succeeded',
                   'digit3succeeded',
                   'digit4succeeded',
                   'digit5succeeded',
                   'digit6succeeded',
                   'digit7succeeded',
                   'digit8succeeded',
                   'digit9succeeded']

# math state operators in string form
opvec = ['+', '-', '/', '*']

# The empty vector of times things have been drawn
times = []


# Getting username and info
database = pickle.load(open('userData/database.p','rb'))
username = raw_input('Please enter your name: ')
if username not in database:
    for i in range(0,10):
        database[username] = {'logins': 1,


                              'digitsAttempted': {
                                  digitsAttempted[0]: 0,
                                  digitsAttempted[1]: 0,
                                  digitsAttempted[2]: 0,
                                  digitsAttempted[3]: 0,
                                  digitsAttempted[4]: 0,
                                  digitsAttempted[5]: 0,
                                  digitsAttempted[6]: 0,
                                  digitsAttempted[7]: 0,
                                  digitsAttempted[8]: 0,
                                  digitsAttempted[9]: 0,
                              },

                              'digitsSucceeded': {
                                  digitsSucceeded[0]: 0,
                                  digitsSucceeded[1]: 0,
                                  digitsSucceeded[2]: 0,
                                  digitsSucceeded[3]: 0,
                                  digitsSucceeded[4]: 0,
                                  digitsSucceeded[5]: 0,
                                  digitsSucceeded[6]: 0,
                                  digitsSucceeded[7]: 0,
                                  digitsSucceeded[8]: 0,
                                  digitsSucceeded[9]: 0,

                              },

                              'rank': 0

                              }

    print('welcome ' + username + '.')

else:
    database[username]['logins'] = database[username]['logins'] + 1

    print('welcome back ' + username + '. \n You have logged in {} times.'.format(database[username]['logins'] ))

pickle.dump(database,open('userData/database.p', 'wb'))

userRecord = database[username]

totalSucceeded = -1

for user in database:
    for digit in database[user]['digitsSucceeded']:
    #     if database[user]['digitsSucceeded'][digit] != 0:
    #         totalSucceeded = totalSucceeded + 1
    # database[user]['rank'] = database[user].get('rank') + totalSucceeded

        rank = database[user]['rank']
        leaderboard[user] = rank
    totalSucceeded = 0
    print user, database[user]['rank']

res = sorted(leaderboard.items(), key = operator.itemgetter(1), reverse=True)



# I feel like I should be making a separate script for a class and shoving
# all of the following functions into it, but I don't have time for that
# so here I am
def Scale(coord, leapMin, leapMax, winMin, winMax):
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
    xBase, yBase, zBase = Handle_Vector_From_Leap(base,divisor)
    xTip, yTip, zTip = Handle_Vector_From_Leap(tip,divisor)
    if ((b == 0) or (b == 3)):
        testData[0, k] = tip[0]
        testData[0, k + 1] = tip[1]
        testData[0, k + 2] = tip[2]
        k = k + 3

    pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, (3-b))


def Handle_Vector_From_Leap(v, divisor): #divisor determines how much room the hand has to move in the window
    #originally 2 to put the hand in the upper left quadrant
    #gonna make it 1 to let the hand move across the whole screen

    global xMin
    global xMax
    global yMin
    global yMax

    xPre = int(v[0])
    yPre = int(v[2]) # why not v[1]?
    zPre = int(v[1])

    # originally pygameWindow.Scale
    xv = Scale(xPre, xMin, xMax, 0, (constants.pygameWindowWidth)/divisor)
    yv = Scale(yPre, yMin, yMax, 0, (constants.pygameWindowDepth)/divisor)
    zv = zPre

    return xv, yv, zv


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
        time.sleep(0.01)
        predictedClass = int(clf.Predict(testData))
        time.sleep(0.01)
       # print(predictedClass)

def CenterData(testData):
    for s in range(0,2):
        allCoords = testData[0,s::3]
        meanVal = allCoords.mean()
        testData[0, s::3] = allCoords - meanVal
    return testData


def chooseMathNum():
    c = random.randint(0, 9)
    d = random.randint(0, 9)

    op = random.randint(0, 3)

    if op == 0:
        mathNum = c + d

        while mathNum > 9:
            d = random.randint(0, 9)
            mathNum = c + d

    elif op == 1:
        mathNum = c - d
        while mathNum < 0:  # if??
            if c == 0:
                c = random.randint(0, 9)
            d = random.randint(0, 9)
            mathNum = c - d

    elif op == 2:
        d = random.randint(1, 9)/1.0
        mathNum = c / d

        intVal = False
        while intVal == False:
            if mathNum%2 == 0 or (mathNum+1)%2 == 0:
                intVal = True
                mathNum = int(mathNum)
                d = int(d)
            else:
                d = random.randint(1,9)/1.0
                mathNum = c/d

    elif op == 3:
        mathNum = c * d
        while mathNum > 9:
            d = random.randint(0, 9)
            mathNum = c * d

    return mathNum, c, d, op


def HandleState0():
    global programState
    global prevState

    pygameWindow.showInitialImage()

    if len(frame.hands) > 0: #I want to make this a boolean: handOverDevice == True
        prevState = 0
        programState = 1

def HandleState1():
    global programState
    global prevState
    global wrongPosition
    global numToSign
    global fakeNum
    global realCoord
    global fakeCoord
    global start
    global prevtime

    wrongPosition = False

    print 'mid', (testData[0,12], testData[0,13], testData[0,14])
    # centeredX: 3-ish, centeredY: 7-ish
    print 'ring', (testData[0,18], testData[0,19], testData[0,20])
    # centeredX: 24-ish, centeredY: 8-ish
    print 'ind', (testData[0, 6], testData[0, 7], testData[0, 8])
    # centeredX: -17-ish, centeredY: 2-ish
    #time.sleep(0.6)

    if len(frame.hands) == 0:
        prevState = 1
        programState = 0

# INDEX FINGER CENTERING
#   Instructions to center hand along x axis
    if testData[0, 6] < -20.5: # originally <-2
        pygameWindow.showMoveLeftImage()
        wrongPosition = True
    elif testData[0, 6] > -15.5:
        pygameWindow.showMoveRightImage()
        wrongPosition = True

#    Instructions to center hand along y axis
    elif testData[0, 7] > 4:
        pygameWindow.showMoveForwardImage()
        wrongPosition = True
    elif testData[0, 7] < -11:
        pygameWindow.showMoveBackwardImage()
        wrongPosition = True

    if not wrongPosition:
        print wrongPosition
        # pygameWindow.showSuccessImage()
        # pygameWindow.Reveal()
        # time.sleep(0.5)
        # pygameWindow.Prepare()



        for i in range(0, 10):
            # if userRecord[digitsSucceeded[i]] == 0:

            # the program is seeing how many times the user has successfully signed.
            # so, consulting the number of succeeded repetitions.
            # if they've done it at least 3 times (in a row?), the program progresses to next digit.

            # if the user has not successfully signed digit i at least 3 times:

            if database[username]['digitsSucceeded'][digitsSucceeded[i]] < thresh:
                start = start + 1

        # choose numToSign based on what numbers have been successfully signed
        if start == 10:
            numToSign = 0
        elif start == 9:
            numToSign = 1
        elif start == 8:
            numToSign = 2
        elif start == 7:
            numToSign = 3
        elif start == 6:
            numToSign = 4
        elif start == 5:
            numToSign = 5
        elif start == 4:
            numToSign = 6
        elif start == 3:
            numToSign = 7
        elif start == 2:
            numToSign = 8
        elif start == 1:
            numToSign = 9

        # choose random fake number to trick with
        fakeNum = random.randint(0, 9)
        while fakeNum == numToSign:
            fakeNum = random.randint(0,9)

        # choose coordinates for the real digit image
        # fake coordinates decided by process of elimination
        realCoord = random.randint(0,1)
        fakeCoord = random.randint(0,1)
        while fakeCoord == realCoord:
            fakeCoord = random.randint(0,1)


    #    print 'successes' + str(database[username][digitsSucceeded[numToSign]])

        # database[username][digitsAttempted[i]] = database[username].get(digitsAttempted[i]) + 1

        #print database[username][digitsAttempted[numToSign]]
        # pickle.dump(database, open('userData/database.p', 'wb'))
        prevtime = time.time()

        start = 0
        prevState = 1
        programState = 4




def HandleState2():
    global programState
    global prevState
    global points
    global times
    global fail #???
    global sec #???
    global prevtime #???

    pygameWindow.showLeaderboard(res)
    pygameWindow.progressBar(points, fail)


    if len(frame.hands) == 0:
        database[username]['digitsAttempted'][digitsAttempted[numToSign]] = database[username]['digitsAttempted'].get(digitsAttempted[numToSign]) + 1
        pickle.dump(database, open('userData/database.p', 'wb'))
        prevState = 2
        programState = 0



    # Just shows the number of times that digit has been attempted
    timesAttempted = str(database[username]['digitsAttempted'][digitsAttempted[numToSign]])
    timesSucceeded = str(database[username]['digitsSucceeded'][digitsSucceeded[numToSign]])
    timesCompared = timesSucceeded + "/" + str(thresh)

   # print times

    pygameWindow.showNumToSign(numToSign)
    pygameWindow.showTimes(timesAttempted, constants.timesAttemptedCoords)

    pygameWindow.showTimes(timesCompared, constants.timesComparedCoords)

    for i in range(0,10):
        achievedNum = str(achieved[i])
        color = 'grey'

        if achieved[i] == i:
            if i == numToSign:
                color = 'black'
            if database[username]['digitsSucceeded'][digitsSucceeded[i]] >= thresh:
                color = 'green'

    # pygameWindow.showTimes(timesSucceeded, constants.timesSucceededCoords)

    # if points == 0:
    #     fail = fail + 1


    prevtime = time.time()


    if database[username]['digitsSucceeded'][digitsSucceeded[numToSign]] < 1:
        if (time.time() - prevtime) < 22:
            # if nowtime < 5:
            #     pygameWindow.fakeOut(numToSign, fakeNum, realCoord, fakeCoord)
            # else:
            #     pygameWindow.showRealDigit(numToSign)

            if fail < 10:
                pygameWindow.fakeOut(numToSign, fakeNum, realCoord, fakeCoord)
            else:
                pygameWindow.showRealDigit(numToSign)
        else:
            pygameWindow.youFailed()

            prevtime = time.time()
            database[username]['digitsAttempted'][digitsAttempted[numToSign]] = database[username]['digitsAttempted'].get(digitsAttempted[numToSign]) + 1


    elif database[username]['digitsSucceeded'][digitsSucceeded[numToSign]] < 2:
        if (time.time() - prevtime) < 14:
            # if fail < 20:
            #     pygameWindow.fakeOut(numToSign, fakeNum, realCoord, fakeCoord)
            # else:
            pygameWindow.showRealDigit(numToSign)
        else:
            pygameWindow.youFailed()
            prevtime = time.time()
            database[username]['digitsAttempted'][digitsAttempted[numToSign]] = database[username]['digitsAttempted'].get(digitsAttempted[numToSign]) + 1


    else: #database[username][digitsSucceeded[numToSign]] < 3:
        if (time.time() - prevtime) > 6:
            # pygameWindow.youFailed()
            # pygameWindow.showFailImage()
            # pygameWindow.Reveal()
            # time.sleep(0.5)
            # pygameWindow.Prepare()
            # fail = 0
            points = 0
            prevtime = time.time()
            database[username]['digitsAttempted'][digitsAttempted[numToSign]] = database[username]['digitsAttempted'].get(digitsAttempted[numToSign]) + 1

    print(predictedClass, points)
    print(time.time() - prevtime)


    time.sleep(0.05)
    if predictedClass == numToSign:
        points = points + 1

        fail = 0 # Maybe this?????
        if points == 15:
            database[username]['digitsSucceeded'][digitsSucceeded[numToSign]] = database[username]['digitsSucceeded'].get(digitsSucceeded[numToSign]) + 1
            database[username]['rank'] = database[username].get('rank') + 1
            print database[username]['digitsSucceeded'][digitsSucceeded[numToSign]]
            pickle.dump(database, open('userData/database.p', 'wb'))

            fail = 0
            points = 0
            prevState = 2
            programState = 3

    else:
        points = 0
        fail = fail + 1
        #pygameWindow.showFailImage()

def HandleState3():
    global programState
    global prevState
    global numToSign
    global mathNum, c, d, op
    global prevtime
    global res

    print prevState
    # can I make you update only a portion of the screen????

    pygameWindow.showSuccessImage()
    pygameWindow.Reveal()
    time.sleep(1)
    pygameWindow.Prepare()

    # totalSucceeded = 0

    for user in database:
        rank = database[user]['rank']
        leaderboard[user] = rank
        print user, database[user]['rank']

    res = sorted(leaderboard.items(), key=operator.itemgetter(1), reverse=True)
    print res

    if len(frame.hands) > 0:
        # MIDDLE FINGER CENTERING
        # If hand off-center in x direction

        if testData[0, 12] < -50:
            wrongPosition = True
        elif testData[0, 12] > 50:
            wrongPosition = True

        # If hand off-center in y direction
        elif testData[0, 13] < -50:
            wrongPosition = True
        elif testData[0, 13] > 50:
            wrongPosition = True

        else:
            wrongPosition = False


        # INDEX FINGER CENTERING
        #   Instructions to center hand along x axis
        # if testData[0, 6] < -30:  # originally <-2
        #     pygameWindow.showMoveLeftImage()
        #     wrongPosition = True
        # elif testData[0, 6] > 0:
        #     pygameWindow.showMoveRightImage()
        #     wrongPosition = True
        #
        #     #    Instructions to center hand along y axis
        # elif testData[0, 7] > 5:
        #     pygameWindow.showMoveForwardImage()
        #     wrongPosition = True
        # elif testData[0, 7] < -15:
        #     pygameWindow.showMoveBackwardImage()
        #     wrongPosition = True


        if wrongPosition:
            prevState = 3
            programState = 1
        else:

            bleh = 0

            if prevState == 2:

                if database[username]['digitsSucceeded'][digitsSucceeded[numToSign]] < thresh:
                    numToSign = numToSign
                else:

                    for i in range(0, 10):
                        # the program is seeing how many times the user has successfully signed.
                        # so, consulting the number of succeeded repetitions.
                        # if they've done it at least 3 times (in a row?), the program progresses to next digit.

                        # if the user has not successfully signed digit i at least 3 times:
                        if database[username]['digitsSucceeded'][digitsSucceeded[i]] < thresh:
                            bleh = bleh + 1

                    # choose numToSign based on what numbers have been successfully signed
                    if bleh == 10:
                        numToSign = 0
                    elif bleh == 9:
                        numToSign = 1
                    elif bleh == 8:
                        numToSign = 2
                    elif bleh == 7:
                        numToSign = 3
                    elif bleh == 6:
                        numToSign = 4
                    elif bleh == 5:
                        numToSign = 5
                    elif bleh == 4:
                        numToSign = 6
                    elif bleh == 3:
                        numToSign = 7
                    elif bleh == 2:
                        numToSign = 8
                    elif bleh == 1:
                        numToSign = 9

                    if database[username]['rank'] >= 40:
                        programState = 4 # the mode selection state

                prevtime = time.time()
                prevState = 3
                programState = 2

            if prevState == 5:
                mathNum, c, d, op = chooseMathNum()

                if mathNum == 0:
                    limit0 = random.randint(0, 10)
                    if limit0 > 2:
                        while mathNum == 0:
                            mathNum, c, d, op = chooseMathNum()

                elif mathNum == 1:
                    limit1 = random.randint(0, 10)
                    if limit1 > 2:
                        while mathNum == 1:
                            mathNum, c, d, op = chooseMathNum()

                eqn = str(c) + ' {} '.format(opvec[op]) + str(d) + ' = __'
                prevState = 3
                programState = 5

    else:
        prevState = 3
        programState = 0

def HandleState4(): # select the game mode
    # if I enable a back button in the other modes, it'll lead here
    global prevtime
    global runtime
    global divisor
    global programState
    global prevState
    global randNum
    global mathNum, c, d, op
    global runScore
    global fail
    global points
    divisor = 1

    print(testData[0,9:12])

    pygameWindow.showModes()
    drawnIndex = Handle_Vector_From_Leap(testData[0,9:12],divisor)
    print(drawnIndex[0:3])
    time.sleep(0.02)

    print 'ind' + str(drawnIndex[0:3]) + ', '

    if (drawnIndex[0] > 350) & (drawnIndex[0] < 360):
        if (drawnIndex[1] > 300) & (drawnIndex[1] < 390):
            # figure out how to make it so they have to stay here for 2 seconds
            mode = 'math'
            pygameWindow.modeSelect(mode)
            mathNum, c, d, op = chooseMathNum()
            prevtime = time.time()
            divisor = 2
            programState = 5

    # originally 365 and 375
    if (drawnIndex[0] > 375) & (drawnIndex[0] < 385):
        if (drawnIndex[1] > 90) & (drawnIndex[1] < 200):
            mode = 'speed'
            pygameWindow.modeSelect(mode)
            prevtime = time.time()
            runtime = time.time()
            randNum = random.randint(0, 9)
            runScore = 0
            points = 0
            fail = 0
            divisor = 2
            programState = 6

    if (drawnIndex[0] > 425) & (drawnIndex[0] < 435):
        if (drawnIndex[1] > 300) & (drawnIndex[1] < 390):
            mode = 'practice'
            pygameWindow.modeSelect(mode)
            prevtime = time.time()
            divisor = 2
            prevState = 4
            programState = 2

def HandleState5(): # math mode
    global mathNum, c, d, op
    global programState
    global prevState
    global divisor
    global points
    divisor = 1.5

    if len(frame.hands) == 0:
        prevState = 5
        programState = 0

    eqn = str(c) + ' {} '.format(opvec[op]) + str(d) + ' = __'



    pygameWindow.showEqn(eqn,mathNum,predictedClass)

    print(predictedClass, mathNum)

    if predictedClass == mathNum:
        time.sleep(0.05)
        points = points + 1
        if points == 8:
            points = 0
            prevState = 5
            programState = 3










    # if you've failed too many times, eqn becomes:
    # eqn = str(c) + ' {} '.format(opvec[op]) + str(d) + ' = ' + str(mathNum)

    # We're gonna have to find a way to make previous program state matter when the success image shows up









def HandleState6(): # speed mode
    global randNum
    global programState
    global prevState
    global points
    global runScore
    global divisor
    global runtime
    global fail
    divisor = 2

    pygameWindow.progressBar(points, fail)

    if (time.time() - prevtime) < 10:
        if (time.time() - runtime) < 5:

            pygameWindow.showRealDigit(randNum)
            pygameWindow.showNumToSign(randNum)
            time.sleep(0.05)
            debugTime = time.time() - runtime
            print debugTime
            print(predictedClass, randNum)
            if predictedClass == randNum:
                time.sleep(0.05)
                fail = 0
                points = points + 1
                if points == 3:
                    runScore = runScore + 1
                    randNum = random.randint(0,9)
                    points = 0
                    fail = 0
                    runtime = time.time()
            else:
                points = 0
                fail = fail + 1
        else:
            randNum = random.randint(0,9)
            points = 0
            runtime = time.time()

        print(int(time.time()-prevtime) - 10)

    else:
        print runScore
        pygameWindow.timeUp()
        prevState = 6
        programState = 4

def HandleState6b():
    pass


            # if nowtime < 5:
            #     pygameWindow.fakeOut(numToSign, fakeNum, realCoord, fakeCoord)
            # else:



                #
                # database[username]['speedrunRecord'] = database[username].get('speedrunRecord') + 1
                #
                # database[username]['digitsSucceeded'][digitsSucceeded[numToSign]] = database[username]['digitsSucceeded'].get(digitsSucceeded[numToSign]) + 1
                # database[username]['rank'] = database[username].get('rank') + 1
                # print database[username]['digitsSucceeded'][digitsSucceeded[numToSign]]
                # pickle.dump(database, open('userData/database.p', 'wb'))
                #


    # if scaled index coordinates enter box X (math)
    # highlight box in green
    # start math mode
    # elif scaled index coordinates enter box Y (random)
    # highlight box in green
    # start random mode
    # if scaled index coordinates enter box Z (practice)
    # highlight box in green
    # start practice mode

    # if the user enters random mode
    # show random numbers for them to sign for 1 minute
    #




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
    elif programState == 4:
        HandleState4()
    elif programState == 5:
        HandleState5()
    elif programState == 6:
        HandleState6()

    pygameWindow.Reveal()  # show drawn material to the user



    # # Instructions to center hand along z axis
    # elif testData[0, 14] < 90:
    #     pygameWindow.showMoveUpImage()
    #     wrongPosition = True
    # elif testData[0,14] > 190:
    #     pygameWindow.showMoveDownImage()
    #     wrongPosition = True

    # MIDDLE FINGER CENTERING
    # Instructions to center hand along x axis
    # if testData[0, 12] > 5: # originally <-2
    #     pygameWindow.showMoveLeftImage()
    #     wrongPosition = True
    # elif testData[0,12] < -2:
    #     pygameWindow.showMoveRightImage()
    #     wrongPosition = True
    #
    # # Instructions to center hand along y axis
    # elif testData[0, 13] < 4:
    #     pygameWindow.showMoveForwardImage()
    #     wrongPosition = True
    # elif testData[0,13] > 15:
    #     pygameWindow.showMoveBackwardImage()
    #     wrongPosition = True
