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
from frameHandling import FRAME_HANDLER

class STATE_HANDLER:

    def __init__(self):
        self.controller = Leap.Controller()
        self.pygameWindow= PYGAME_WINDOW()
        self.frameHandler = FRAME_HANDLER()
        self.testData = self.frameHandler.testData
        self.frame = self.controller.frame()
        self.programState = 0
        self.wrongPosition = True

    def HandleState0(self, frame):
        self.pygameWindow.showInitialImage()

        if len(frame.hands) > 0:  # I want to make this a boolean: handOverDevice == True
            self.programState = 1

    def HandleState1(self, frame):
        global numToSign

        self.wrongPosition = False

        print(self.testData[0, 12],    # printing 0 here, but real numbers in frameHandling
              self.testData[0, 13],
              self.testData[0, 14])

        if len(frame.hands) == 0:
            self.programState = 0

        # # Hardcoded; will fix later
        # # Instructions to center hand along x axis
        if self.testData[0, 12] < -4:
            self.pygameWindow.showMoveLeftImage()
            self.wrongPosition = True
        elif self.testData[0, 12] > 4:
            self.pygameWindow.showMoveRightImage()
            self.wrongPosition = True
        #
        # # Instructions to center hand along y axis
        # elif self.frameHandler.testData[0, 13] < 4:
        #     self.pygameWindow.showMoveForwardImage()
        #     self.wrongPosition = True
        # elif self.frameHandler.testData[0, 13] > 15:
        #     self.pygameWindow.showMoveBackwardImage()
        #     self.wrongPosition = True
        #
        # if not wrongPosition:
        #     self.pygameWindow.showSuccessImage()
        #     self.pygameWindow.Reveal()
        #     time.sleep(0.5)
        #     self.pygameWindow.Prepare()
        #
        #     numToSign = random.randint(0, 9)
        #     self.programState = 2


