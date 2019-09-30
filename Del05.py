import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')

import Leap

import constants
from pygameWindow_Del03 import PYGAME_WINDOW_Del03

from Recorder import RECORDER


# Creating an instance of the DELIVERABLE class
recorder = RECORDER(constants.x, constants.y, constants.xMin, constants.xMax, constants.yMin, constants.yMax)

recorder.Clear_User_Data()

recorder.Run_Forever()
