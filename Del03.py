import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')

import Leap

import constants
from pygameWindow_Del03 import PYGAME_WINDOW_Del03

from deliverable import DELIVERABLE


# Creating an instance of the DELIVERABLE class
deliverable = DELIVERABLE(constants.x, constants.y, constants.xMin, constants.xMax, constants.yMin, constants.yMax)

deliverable.Clear_User_Data()

deliverable.Run_Forever()
