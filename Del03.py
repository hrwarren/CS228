import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')

import Leap

import constants
import pygameWindow

from deliverable import DELIVERABLE

# circle position and axes
x = 0
y = 0


# Creating an instance of the DELIVERABLE class
deliverable = DELIVERABLE(x, y, constants.xMin, constants.xMax, constants.yMin, constants.yMax)
exit()

runStatus = True  # this is now a switch


while runStatus:
    pygameWindow.Prepare()  # wipe window to prepare for drawing

    frame = deliverable.controller.frame()

    deliverable.Handle_Frame_Init()

    # Why does Bongard want this function call to be in Handle_Bone() instead of out here?
    #pygameWindow.Draw_Black_Line(xBase, xTip, yBase, yTip)

    pygameWindow.Reveal()  # show drawn material to the user