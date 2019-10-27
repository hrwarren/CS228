import sys
sys.path.insert(0, '..')
sys.path.insert(1, '../x86')

import Leap

from frameHandling import FRAME_HANDLER
from pygameWindow import PYGAME_WINDOW
from stateHandling import STATE_HANDLER

# construct the class with functions to handle frames
frameHandler = FRAME_HANDLER()

# construct the class with functions to handle program states
stateHandler = STATE_HANDLER()

# construct the class that deals with graphics
pygameWindow = PYGAME_WINDOW()

# initialize the Leap controller and frame
controller = Leap.Controller()
frame = controller.frame()

while True:

    pygameWindow.Prepare()
    frame = controller.frame()

    frameHandler.Handle_Frame_Init(frame)

    if stateHandler.programState == 0:
        stateHandler.HandleState0(frame)
    if stateHandler.programState == 1:
        stateHandler.HandleState1(frame)
    # if stateHandler.programState == 2:
    #     stateHandler.HandleSTate2(frame)
    print stateHandler.programState

    pygameWindow.Reveal()
