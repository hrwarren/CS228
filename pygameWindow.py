import pygame
import time
import constants
import sys
import random
import numpy as np
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')
import Leap #still not able to import Leap for some reason???

class PYGAME_WINDOW:
    #PYGAME_WINDOW class's constructor 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowDepth)) #note: 300,100 represents screen height and width
        self.controller = Leap.Controller()
        self.frame = self.controller.frame()
        self.font = pygame.font.Font('freesansbold.ttf',32)
        self.eqnfont = pygame.font.Font('freesansbold.ttf', 80)

    def Prepare(self):
        pygame.event.get()
        self.screen.fill(constants.white) #makes window white
    
    def Reveal(self):  
        pygame.display.update()
    
    def Draw_Black_Circle(self, x, y):
        # axis control (leapMin and leapMax)
        if x < 0:
            x = 0
        if x > constants.pygameWindowWidth:
            x = constants.pygameWindowWidth
        if y < 0:
            y = 0
        if y > constants.pygameWindowDepth:
            y = constants.pygameWindowDepth
        pygame.draw.circle(self.screen, constants.black, [x,y], 20) #args are (screen, color, coordinates, size)

    def Draw_Black_Line(self, xBase, yBase, xTip, yTip, b):
        pygame.draw.line(self.screen, constants.black, [xBase, yBase], [xTip, yTip], b)

    #copied Scale() over from Del01
    def Scale(self, coord, leapMin, leapMax, winMin, winMax):  # this Min could be zero dammit
        screenwidth = winMax - winMin
        scalar = 3
        ratio = (((scalar * coord) + ((leapMax - leapMin) / 2)) / (leapMax - leapMin))
        print(ratio)
        return int((ratio) * (screenwidth))

    def showInitialImage(self):
        image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\HandOverLeapVisual_cropped.jpg')
        self.screen.blit(image, constants.startingImageCoords)

    def showMoveRightImage(self):
        image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveRight.jpg')
        self.screen.blit(image, constants.moveRightImageCoords)

    def showMoveLeftImage(self):
        image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveLeft.jpg')
        self.screen.blit(image, constants.moveLeftImageCoords)

    def showMoveForwardImage(self):
        image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveForward.jpg')
        self.screen.blit(image, constants.moveForwardImageCoords)

    def showMoveBackwardImage(self):
        image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveBackward.jpg')
        self.screen.blit(image, constants.moveBackwardImageCoords)

    def showMoveUpImage(self):
        image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveUp.jpg')
        self.screen.blit(image, constants.moveUpImageCoords)

    def showMoveDownImage(self):
        image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveDown.jpg')
        self.screen.blit(image, constants.moveDownImageCoords)

    def showSuccessImage(self):
        image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Success.jpg')
        # image = pygame.transform.scale(image, (150,150))
        self.screen.blit(image, constants.successImageCoords)

    def showFailImage(self):
        image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Fail.jpg')
        self.screen.blit(image, constants.successImageCoords)

    def showNumToSign(self, num):

        # For showing each number indvidiually
        # imageDirectory = 'C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num'
        # numImage = pygame.image.load(imageDirectory + '{}'.format(num) + '.jpg')
        # self.screen.blit(numImage, constants.numImageCoords)

        numImage = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num{}.jpg'.format(num))
        self.screen.blit(numImage, constants.numImageCoords)

    def showRealDigit(self,num):
        digitImage = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit{}.jpg'.format(num))
        self.screen.blit(digitImage, constants.digitImageCoords)

    def fakeOut(self, num, fake1, realIndex, fakeIndex):
        # display real sign at one of 2 potential places
        coordVec = constants.coordVec
        digitImage = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit{}.jpg'.format(num))
        self.screen.blit(digitImage, coordVec[realIndex])
        # coordVec = np.delete(coordVec, 0, realIndex)

        # display fake sign #1 at one of the 2 remaining places
        fakeImage = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit{}.jpg'.format(fake1))

        self.screen.blit(fakeImage, coordVec[fakeIndex])
        coordVec = np.delete(coordVec, 0)

        #self.screen.blit('?', constants.qCoords)

    def clearDigits(self):
        pygame.draw.rect(self.screen, constants.white, constants.clear)

    # def showOutline(self):
    #     self.pygame.draw.rect(self.screen, constants.red, )

    def showTimes(self, times, coords): # for displaying the number of times a number has been tried or succeeded
        times = self.font.render(times, True, constants.black)
        # times = times.get_rect()
        self.screen.blit(times, coords)

    def youFailed(self, prevtime):
        print (time.time() - prevtime)
        self.showFailImage()
        self.Reveal()
        time.sleep(0.5)
        self.Prepare()
        fail = 0
        points = 0

        return fail, points

    def showTotalAchieved(self, achievedNum, color, i):

        if color == 'green':
            achievedNum = self.font.render(str(achievedNum), True, constants.green)
            self.screen.blit(achievedNum, constants.achievedCoords[i])

        elif color == 'grey':
            achievedNum = self.font.render(achievedNum, True, constants.grey)
            self.screen.blit(achievedNum, constants.achievedCoords[i])

        else:
            achievedNum = self.font.render(achievedNum, True, constants.black)
            self.screen.blit(achievedNum, constants.achievedCoords[i])

    def showLeaderboard(self, rankList):


        label = []
        for player in rankList:
            if player[1] != 0:
                rank = str(rankList.index(player) + 1) + '. ' + str(player[0]) + ', ' + str(player[1])
                label.append(self.font.render(rank, True, constants.black))

        if len(label) < 6:
            for line in range(0,len(label)):
                self.screen.blit(label[line], (constants.boardCoords[0], constants.boardCoords[1]+(30*line)))
        else:
            for line in range(0,6):
                self.screen.blit(label[line], (constants.boardCoords[0], constants.boardCoords[1] + (30 * line)))

    def progressBar(self, points, fails):

        star = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Star.jpg')
        star = pygame.transform.scale(star, (30,30))
        self.screen.blit(star, constants.starCoords)

        pygame.draw.rect(self.screen,constants.grey,constants.baseBar)
        gr = False

        #should be able to make these work with elif but apparently not
        if (points >= 3) & (points < 6):
            # if points < 7:
            gr = True
            pygame.draw.rect(self.screen, constants.green, constants.greenInc[0])


        if (points >= 6) & (points < 8):
            #if points < 8:
            gr = True
            for i in range(0,2):
                pygame.draw.rect(self.screen, constants.green, constants.greenInc[i])

        if points >= 8:
            gr = True
            for i in range (0,3):
                pygame.draw.rect(self.screen, constants.green, constants.greenInc[i])

        if (fails >= 3) & (fails < 9):
            if gr == False:
                pygame.draw.rect(self.screen, constants.red, constants.redInc[0])

        if (fails >= 9) & (fails < 16):
            if gr == False:
                for i in range(0,2):
                    pygame.draw.rect(self.screen, constants.red, constants.redInc[i])

        if fails >= 16:
            if gr == False:
                for i in range(0,3):
                    pygame.draw.rect(self.screen, constants.red, constants.redInc[i])




# SO I WAS TODAY YEARS OLD WHEN I LEARNED I CAN UPDATE JUST ONE PORTION OF THE SCREEN
# WHY WAS I NEVER TOLD THIS
# I'll incorporate this at some point but I don't think I'll have time for this deliverable

    def showModes(self):
        mathBox = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\mathBox.jpg')
        mathBox = pygame.transform.scale(mathBox, (100, 100))
        self.screen.blit(mathBox, constants.mathBox)

        speedBox = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\speedBox.jpg')
        speedBox = pygame.transform.scale(speedBox, (100, 100))
        self.screen.blit(speedBox, constants.speedBox)

        practiceBox = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\practiceBox.jpg')
        practiceBox = pygame.transform.scale(practiceBox, (100, 100))
        self.screen.blit(practiceBox, constants.practiceBox)

    def modeSelect(self, mode):

        if mode == 'math':
            pygame.draw.rect(self.screen, constants.green, constants.mathRect, 3)
            self.Reveal()
            time.sleep(0.5)
            self.Prepare()
            print 'math chosen'

        elif mode == 'speed':
            pygame.draw.rect(self.screen, constants.green, constants.speedRect, 3)
            self.Reveal()
            time.sleep(0.5)
            self.Prepare()
            print 'speedrun chosen'

        elif mode == 'practice':
            pygame.draw.rect(self.screen, constants.green, constants.practiceRect, 3)
            self.Reveal()
            time.sleep(0.5)
            self.Prepare()
            print 'practice chosen'

    def timeUp(self):
        msg = 'Time is Up!'
        msg = self.font.render(msg, True, constants.red)
        self.screen.blit(msg, constants.timeUpCoords)

        self.Reveal()
        time.sleep(0.5)
        self.Prepare()

        print 'time Up'

    def showEqn(self, eqn, mathNum, predictedNum):


        eqn = self.eqnfont.render(eqn, True, constants.black)
        self.screen.blit(eqn, constants.eqnCoords)

        ansColor = constants.red

        if predictedNum == mathNum:
            ansColor = constants.green

        ans = str(predictedNum)
        ans = self.eqnfont.render(ans, True, ansColor)
        self.screen.blit(ans, constants.ansCoords)


        # fill in line with predictedNum
        # if predictedNum != mathNum
        # show predictedNum in red


        # if you do too badly, it shows you the numeral
        #

        # if you succeed, you fill in the ___ with your signed number

