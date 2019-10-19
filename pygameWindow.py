import pygame
import time
import constants
import sys
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
        self.screen.blit(image, constants.successImageCoords)

    def showNumToSign(self, num):    # will also contain num as a parameter once I have a photo for each sign

        # For showing each number indvidiually
        # imageDirectory = 'C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num'
        # numImage = pygame.image.load(imageDirectory + '{}'.format(num) + '.jpg')
        # self.screen.blit(numImage, constants.numImageCoords)

        digitImage = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Digit{}.jpg'.format(num))
        self.screen.blit(digitImage, constants.digitImageCoords)

        numImage = pygame.image.load('C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\Num{}.jpg'.format(num))
        self.screen.blit(numImage, constants.numImageCoords)


        # pygame.draw.polygon(self.screen, constants.grey, [(600,600), (600,400), (400,400), (400,600)])
        # pygame.draw.polygon(self.screen, constants.green, [(580,510),(580,490),(40)])


    # def Scale(self,coord, leapMin, leapMax, winMin, winMax):  # this Min could be zero dammit
    #     screenwidth = winMax - winMin
    #     # scalar = 3 would normally multiply coord
    #     coordScaled = ((((coord - (leapMax - leapMin)) * screenwidth)) / 2) / (leapMax - leapMin)
    #     return (int(coordScaled))

    # def Handle_Vector_From_Leap(self, v):
    #     xPre = int(v[0])
    #     yPre = int(v[2])  # why not v[1]?
    #     xv = self.Scale(xPre, constants.xMin, constants.xMax, 0, constants.pygameWindowWidth)
    #     yv = self.Scale(yPre, constants.yMin, constants.yMax, 0, constants.pygameWindowDepth)
    #     return (xv, yv)
    #
    # def Handle_Finger(self, finger):
    #     for b in range(0, 4):
    #         bone = finger.bone(b)
    #         self.Handle_Bone(bone)
    #
    # def Handle_Bone(self, bone):
    #     base = bone.prev_joint
    #     tip = bone.next_joint
    #     self. xBase, self.yBase = self.Handle_Vector_From_Leap(base)
    #     self.xTip, self.yTip = self.Handle_Vector_From_Leap(tip)
    #     #self.Draw_Black_Line(xBase, yBase, xTip, yTip)
    #     print(self.xBase, self.yBase)
    #     print(self.xTip, self.yTip)
    #
    # def Handle_Frame_Init(self):  # This function works in Del01, but fails if I move it to pygameWindow
    #     global x
    #     global y
    #
    #     handList = self.frame.hands
    #     if len(handList) > 0:  # use isempty to track values of objects in the list
    #         handList = self.frame.hands
    #         for hand in handList:
    #             fingers = hand.fingers
    #             for finger in fingers:
    #
    #                 # axis control (leapMin and leapMax)
    #                 if x < constants.xMin:
    #                     xMin = x
    #                 if x > constants.xMax:
    #                     xMax = x
    #                 if y < constants.yMin:
    #                     yMin = y
    #                 if y > constants.yMax:
    #                     yMax = y
    #
    #                 self.Handle_Finger(finger)


    #def Handle_Frame_Update(self, frame):