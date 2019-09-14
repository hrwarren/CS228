import pygame
import constants
import sys

sys.path.insert(0, '..')
sys.path.insert(1, '../x86')
import Leap  # still not able to import Leap for some reason???


class PYGAME_WINDOW_Del03:
    # PYGAME_WINDOW class's constructor
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth, constants.pygameWindowDepth))  # note: 300,100 represents screen height and width
        self.controller = Leap.Controller()
        self.frame = self.controller.frame()

    def Prepare(self):
        pygame.event.get()
        self.screen.fill(constants.white)  # makes window white

    def Reveal(self):
        pygame.display.update()

    def Draw_Line(self, color, xBase, yBase, xTip, yTip, b):
        pygame.draw.line(self.screen, color, [xBase, yBase], [xTip, yTip], b)



    # def Handle_Frame_Update(self, frame):
