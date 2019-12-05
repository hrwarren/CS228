import pygame
import time
import constants
import sys
import random
import numpy as np
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')

import pygame_textInput
import gameImages

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
        self.pics = gameImages.PICS()


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
        # image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\HandOverLeapVisual_cropped.jpg')
        # self.screen.blit(image, constants.startingImageCoords)
        self.screen.blit(self.pics.initialImage, constants.startingImageCoords)

    def showMoveRightImage(self):
        # image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveRight.jpg')
        # self.screen.blit(image, constants.moveRightImageCoords)
        self.screen.blit(self.pics.moveRight, constants.moveRightImageCoords)

    def showMoveLeftImage(self):
        # image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveLeft.jpg')
        # self.screen.blit(image, constants.moveLeftImageCoords)
        self.screen.blit(self.pics.moveLeft, constants.moveLeftImageCoords)

    def showMoveForwardImage(self):
        # image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveForward.jpg')
        # self.screen.blit(image, constants.moveForwardImageCoords)
        self.screen.blit(self.pics.moveForward, constants.moveForwardImageCoords)

    def showMoveBackwardImage(self):
        # image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\MoveBackward.jpg')
        # self.screen.blit(image, constants.moveBackwardImageCoords)
        self.screen.blit(self.pics.moveBackward, constants.moveBackwardImageCoords)

    def showSuccessImage(self):
        # image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Success.jpg')
        # # image = pygame.transform.scale(image, (150,150))
        # self.screen.blit(image, constants.successImageCoords)
        self.screen.blit(self.pics.success, constants.successImageCoords)
        pygame.display.update((420, 0, 400, 400))

    def showFailImage(self):
        # image = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Fail.jpg')
        # self.screen.blit(image, constants.successImageCoords)
        self.screen.blit(self.pics.fail, constants.successImageCoords)

    def showNumToSign(self, num):
        # For showing each number indvidiually
        # numImage = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num{}.jpg'.format(num))
        # self.screen.blit(numImage, constants.numImageCoords)
        self.screen.blit(self.pics.numerals[num], constants.numImageCoords)

    def showRealDigit(self,num):
        # digitImage = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit{}.jpg'.format(num))
        # self.screen.blit(digitImage, constants.digitImageCoords)
        self.screen.blit(self.pics.digits[num], constants.digitImageCoords)

    def clear(self, coords):
        pygame.draw.rect(self.screen, constants.blue, coords)

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

    def showLeaderboard(self, rankList, mode):

        if mode == 'speed':
            coords = constants.speederboardCoords
        if mode == 'practice':
            coords = constants.leaderboardCoords

        label = []
        for player in rankList:
            if player[1] != 0:
                rank = str(rankList.index(player) + 1) + '. ' + str(player[0]) + ', ' + str(player[1])
                label.append(self.font.render(rank, True, constants.black))


        if len(label) < 6:
            for line in range(0,len(label)):
                self.screen.blit(label[line], (coords[0], coords[1]+(30*line)))
        else:
            for line in range(0,6):
                self.screen.blit(label[line], (coords[0], coords[1] + (30 * line)))

        #
        # if len(label) < 6:
        #     for line in range(0,len(label)):
        #         self.screen.blit(label[line], (constants.boardCoords[0], constants.boardCoords[1]+(30*line)))
        # else:
        #     for line in range(0,6):
        #         self.screen.blit(label[line], (constants.boardCoords[0], constants.boardCoords[1] + (30 * line)))

    def progressBar(self, points, fails):

        # star = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Star.jpg')
        # star = pygame.transform.scale(star, (30,30))
        self.screen.blit(self.pics.star, constants.starCoords)

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

    def showModes(self, rank):  #formerly took self, ready(bool)
        self.screen.blit(self.pics.practiceBox, constants.practiceBox)

        if rank >= 15 and rank < 30 :

            # speedBox = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\speedBox.jpg')
            # speedBox = pygame.transform.scale(speedBox, (100, 100))
            self.screen.blit(self.pics.speedBox, constants.speedBox)

            pygame.draw.rect(self.screen, constants.grey, constants.mathRect)
            self.screen.blit(self.pics.lockedImage, constants.mathRect)

        elif rank >= 30:
            # speedBox = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\speedBox.jpg')
            # speedBox = pygame.transform.scale(speedBox, (100, 100))
            self.screen.blit(self.pics.speedBox, constants.speedBox)

            # mathBox = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\mathBox.jpg')
            # mathBox = pygame.transform.scale(mathBox, (100, 100))
            self.screen.blit(self.pics.mathBox, constants.mathBox)

        else:
            # Show all other modes as locked
            self.screen.blit(self.pics.lockedImage, constants.mathRect)
            self.screen.blit(self.pics.lockedImage, constants.speedRect)



    def modeSelect(self, mode):
        pause = 0.3

        if mode == 'math':
            pygame.draw.rect(self.screen, constants.green, constants.mathRect, 3)
            self.Reveal()
            time.sleep(pause)
            self.Prepare()
            print 'math chosen'

        elif mode == 'speed':
            pygame.draw.rect(self.screen, constants.green, constants.speedRect, 3)
            self.Reveal()
            time.sleep(pause)
            self.Prepare()
            print 'speedrun chosen'

        elif mode == 'practice':
            pygame.draw.rect(self.screen, constants.green, constants.practiceRect, 3)
            self.Reveal()
            time.sleep(pause)
            self.Prepare()
            print 'practice chosen'

    def timeUp(self, runScore, missed):

        # clock = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\clock.jpg')
        # clock = pygame.transform.scale(clock, (120,144))


        redZero = self.eqnfont.render('= 0', True, constants.red)
        self.screen.blit(redZero, constants.redZeroCoords)

        # pixels = pygame.PixelArray(clock)
        # pixels.replace(constants.black, (0,0,255))
        # del pixels
        self.screen.blit(self.pics.speedBox, constants.timeUpCoords) #formerly self.pics.clock

        #check = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Success.jpg')
        check = pygame.transform.scale(self.pics.success, (50,50))
        self.screen.blit(check, constants.checkCoords)

        runScore = str(runScore)
        runScore = self.font.render(runScore, True, constants.black)
        self.screen.blit(runScore, constants.scoreCoords)

        #redX = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Fail.jpg')
        redX = pygame.transform.scale(self.pics.fail, (50,50))
        self.screen.blit(redX, constants.redXCoords)

        missed = str(missed)
        missed = self.font.render(missed, True, constants.black)
        self.screen.blit(missed, constants.missedCoords)





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

        # backBtn = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\prevBtn.jpg')
        # backBtn = pygame.transform.scale(backBtn, (60,30))
        self.screen.blit(self.pics.backBtn, constants.backBtnCoords)

    def showCountDown(self, timeLeft, runScore):

        # check = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Success.jpg')
        check = pygame.transform.scale(self.pics.success, (30,30))
        self.screen.blit(check, constants.duringCheckCoords)

        runScore = str(runScore)
        runScore = self.font.render(runScore, True, constants.black)
        self.screen.blit(runScore, constants.correctCoords)

        #clock = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\speedBox.jpg')
        clock = pygame.transform.scale(self.pics.clock, (100, 100))
        self.screen.blit(clock, constants.clockCoords)

        timeColor = constants.black
        if timeLeft == 0:
            timeColor = constants.red
        timeLeft = '= ' + str(timeLeft)
        timeLeft = self.eqnfont.render(timeLeft, True, timeColor)
        self.screen.blit(timeLeft, constants.timerCoords)

    def loginScreen(self):
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
                self.screen.blit(self.pics.unlockedImage, constants.lockCoords)

            else:
                self.screen.blit(self.pics.lockedImage, constants.lockCoords)

            pygame.display.flip()
            self.clock.tick(30)
        time.sleep(0.25)


        return text

    def showAchievements(self, rank, speedRecord, mathScore):

        j = 0


        # badgeBox

        badgeBox = pygame.Rect(constants.boxCoords)
        pygame.draw.rect(self.screen, constants.black, badgeBox, 2)
        self.screen.blit(self.pics.trophy, constants.trophyCoords)
        self.screen.blit(self.pics.pbTag, constants.pbTagCoords)
        self.screen.blit(self.pics.sbTag, constants.sbTagCoords)
        self.screen.blit(self.pics.mbTag, constants.mbTagCoords)





        if rank >= 15:
            self.screen.blit(self.pics.b[0], constants.pb0Coords)
            if rank >= 30:
                self.screen.blit(self.pics.b[1], constants.pb1Coords)
                if rank >= 45:
                    self.screen.blit(self.pics.b[2], constants.pb2Coords)

        if speedRecord >= 3:
            self.screen.blit(self.pics.b[0], constants.sb0Coords)
            if speedRecord >= 5:
                self.screen.blit(self.pics.b[1], constants.sb1Coords)
                if speedRecord >= 10:
                    self.screen.blit(self.pics.b[2], constants.sb2Coords)

        if mathScore >= 10:
            self.screen.blit(self.pics.b[0], constants.mb0Coords)
            if rank >= 20:
                self.screen.blit(self.pics.b[1], constants.mb1Coords)
                if rank >= 30:
                    self.screen.blit(self.pics.b[2], constants.mb2Coords)

    def showLevelUp(self):
        self.screen.fill(constants.white)

        self.screen.blit(self.pics.practiceBox, constants.practiceBox)
        self.screen.blit(self.pics.lockedImage, constants.speedBox)
        self.screen.blit(self.pics.lockedImage, constants.mathBox)

        self.Reveal()

        #time.sleep(2)



        #Show the unlocking cutscene
        #self.screen.fill(constants.white)


        self.screen.blit(self.pics.practiceBox, constants.practiceBox)

        background = pygame.Surface((self.screen.get_rect().width, self.screen.get_rect().height))
        background.fill((0, 0, 0))
        image = self.pics.lockedImage.convert()
        rect = image.get_rect()

        # i = 255
        # while True:
        #     image.set_alpha(i)
        #     self.screen.fill((255, 255, 255))
        #     self.screen.blit(background, background.get_rect())
        #     self.screen.blit(image, rect)
        #     pygame.time.delay(20)
        #     i -= 1


        pygame.display.update()
        #
        # lock = self.pics.lockedImage
        # backgrnd = pygame.Surface((self.screen.get_size()))
        # backgrnd.fill(constants.white)
        #
        # lock = lock.convert()
        # rect = lock.get_rect()
        #
        # opaque = True
        # i = 255
        # while opaque:
        #     lock.set_alpha(i)
        #     print i
        #     self.screen.fill(constants.white)
        #     self.screen.blit(backgrnd, backgrnd.get_rect())
        #     self.screen.blit(lock, rect)
        #     i -= 1
        #     if i == -2:
        #         opaque = False
        #
        #     pygame.display.update()
        #     pygame.time.Clock().tick(60)


        # pygame.draw.rect(self.screen, constants.white, constants.mathRect)
        # self.screen.blit(self.pics.unlockedImage, constants.mathRect)
        # print 1
        # pygame.draw.rect(self.screen, constants.white, constants.speedRect)
        # self.screen.blit(self.pics.unlockedImage, constants.speedRect)
        # print 2

        # pygame.display.update(constants.mathRect)
        # pygame.display.update(constants.speedRect)
        #
        #
        # self.screen.blit(self.pics.mathBox, constants.mathBox)
        # self.screen.blit(self.pics.speedBox, constants.speedBox)

        self.Reveal()

        time.sleep(1)



