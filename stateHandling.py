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
        # self.testData = self.frameHandler.testData
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

        print(self.frameHandler.testData[0, 12],    # printing 0 here, but real numbers in frameHandling
              self.frameHandler.testData[0, 13],
              self.frameHandler.testData[0, 14])

        print()

        if len(frame.hands) == 0:
            self.programState = 0

        # Hardcoded; will fix later
        # Instructions to center hand along x axis
        if self.frameHandler.testData[0, 6] < -20.5:
            self.pygameWindow.showMoveLeftImage()
            self.wrongPosition = True
        elif self.frameHandler.testData[0, 6] > -15.5:
            self.pygameWindow.showMoveRightImage()
            self.wrongPosition = True


        # Instructions to center hand along y axis
        elif self.frameHandler.testData[0, 7] > 4:
            self.pygameWindow.showMoveForwardImage()
            self.wrongPosition = True
        elif self.frameHandler.testData[0, 7] < -11:
            self.pygameWindow.showMoveBackwardImage()
            self.wrongPosition = True

        if not self.wrongPosition:
            print self.wrongPosition
            self.pygameWindow.showSuccessImage()
            self.pygameWindow.Reveal()
            time.sleep(0.5)
            self.pygameWindow.Prepare()


