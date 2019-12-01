import pygame
import time
import constants
import sys
import random
import numpy as np
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')

import pygame_textInput

import Leap #still not able to import Leap for some reason???

class PYGAME_WINDOW:
    #PYGAME_WINDOW class's constructor 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,constants.pygameWindowDepth)) #note: 300,100 represents screen height and width
        self.controller = Leap.Controller()
        self.frame = self.controller.frame()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('freesansbold.ttf',32)
        self.eqnfont = pygame.font.Font('freesansbold.ttf', 80)
        self.textInput = pygame_textInput.TextInput()

    def Prepare(self):
        pygame.event.get()
        self.screen.fill(constants.white) #makes window white
    
    def Reveal(self):  
        pygame.display.update()

    def Draw_Black_Line(self, xBase, yBase, xTip, yTip, b):
        pygame.draw.line(self.screen, constants.black, [xBase, yBase], [xTip, yTip], b)

    #copied Scale() over from Del01
    def Scale(self, coord, leapMin, leapMax, winMin, winMax):  # this Min could be zero dammit
        screenwidth = winMax - winMin
        scalar = 3
        ratio = (((scalar * coord) + ((leapMax - leapMin) / 2)) / (leapMax - leapMin))
        print(ratio)
        return int((ratio) * (screenwidth))


    # Intro image functions

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

    def clear(self, coords):
        pygame.draw.rect(self.screen, constants.blue, coords)

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

    def showModes(self, ready):
        practiceBox = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\practiceBox.jpg')
        practiceBox = pygame.transform.scale(practiceBox, (100, 100))
        self.screen.blit(practiceBox, constants.practiceBox)

        if ready:

            mathBox = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\mathBox.jpg')
            mathBox = pygame.transform.scale(mathBox, (100, 100))
            self.screen.blit(mathBox, constants.mathBox)

            speedBox = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\speedBox.jpg')
            speedBox = pygame.transform.scale(speedBox, (100, 100))
            self.screen.blit(speedBox, constants.speedBox)

        else:

            pygame.draw.rect(self.screen, constants.grey, constants.mathRect)
            pygame.draw.rect(self.screen, constants.grey, constants.speedRect)


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

    def timeUp(self, runScore, missed):
        msg = 'Time is Up!'
        msg = self.font.render(msg, True, constants.red)
        self.screen.blit(msg, constants.timeUpCoords)

        check = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Success.jpg')
        check = pygame.transform.scale(check, (50,50))
        self.screen.blit(check, constants.checkCoords)

        runScore = str(runScore)
        runScore = self.font.render(runScore, True, constants.black)
        self.screen.blit(runScore, constants.scoreCoords)

        redX = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Fail.jpg')
        redX = pygame.transform.scale(redX, (50,50))
        self.screen.blit(redX, constants.redXCoords)

        missed = str(missed)
        missed = self.font.render(missed, True, constants.black)
        self.screen.blit(missed, constants.missedCoords)

        # self.Reveal()
        # time.sleep(0.5)
        # self.Prepare()

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

    def showBackBtn(self):

        backBtn = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\prevBtn.jpg')
        backBtn = pygame.transform.scale(backBtn, (60,30))
        self.screen.blit(backBtn, constants.backBtnCoords)

    def showCountDown(self, timeLeft, runScore):

        runScore = str(runScore)
        runScore = self.font.render(runScore, True, constants.black)
        self.screen.blit(runScore, constants.scoreCoords)

        timeColor = constants.black
        if timeLeft == 0:
            timeColor = constants.red
        timeLeft = str(timeLeft)
        timeLeft = self.eqnfont.render(timeLeft, True, timeColor)
        self.screen.blit(timeLeft, constants.timerCoords)

    def loginScreen(self):
        lockedImage = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\locked.jpg')
        lockedImage = pygame.transform.scale(lockedImage, constants.lockSize)

        unlockedImage = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\unlocked.jpg')
        unlockedImage = pygame.transform.scale(unlockedImage, constants.lockSize)

        text = ''
        input_box = pygame.Rect(300, 300, 140, 32)
        color = constants.black
        done = False
        unlocked = False

        while not done:

            text = self.textInput.get_text()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print text
                        unlocked = True
                        done = True

                    if event.key == pygame.K_0:
                        exit()

            self.textInput.update(events)

            self.screen.fill((255, 255, 255))

            # Render the current text.
            txt_surface = self.textInput.get_surface()

            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width

            # Blit the text.
            self.screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

            # Blit the input_box rect.
            pygame.draw.rect(self.screen, color, input_box, 2)

            # Blit the lock/unlock image
            if unlocked:
                pixels = pygame.PixelArray(unlockedImage)
                pixels.replace(constants.black, constants.green)
                del pixels
                self.screen.blit(unlockedImage, constants.lockCoords)

            else:
                self.screen.blit(lockedImage, constants.lockCoords)

            pygame.display.flip()
            self.clock.tick(30)
        time.sleep(3)


        return text


        # fill in line with predictedNum
        # if predictedNum != mathNum
        # show predictedNum in red


        # if you do too badly, it shows you the numeral
        #

        # if you succeed, you fill in the ___ with your signed number

