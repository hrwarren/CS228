import time
import random
import constants
import pygameWindow
import Del07
import pygame, sys

random.seed()

pygameWindow = pygameWindow.PYGAME_WINDOW()
#
# while True:
#     # pygameWindow.Prepare()
#     pygameWindow.showLevelUp()
#     # pygameWindow.Reveal()

# pygame.init()
# window=pygame.display.set_mode((1500, 800))
# background=pygame.Surface((window.get_rect().width, window.get_rect().height))
# background.fill((0, 0, 0))
# image=pygameWindow.pics.lockedImage.convert()
# rect=image.get_rect()
#
# i=255
# while True:
#     image.set_alpha(i)
#     window.fill((255, 255, 255))
#     window.blit(background, background.get_rect())
#     window.blit(image, rect)
#     pygame.time.delay(20)
#     i-=1
#     if i==0:
#         exit()
#     pygame.display.update()
#

mathScore = Del07.database['rose']['mathScore'].get('total')
c,d,opvec,mathNum = Del07.chooseMathNum(mathScore)

while True:
    c, d, opvec, mathNum = Del07.chooseMathNum(mathScore)
    Del07.HandleState0()

