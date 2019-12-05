#Constants for screen size
pygameWindowWidth = 800
pygameWindowDepth = 800

#Constants for color
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
grey = (192,192,192)

#Login screen locations
lockCoords = (345, 100)
lockSize = (100, 110)

#Where to display the helpful images
startingImageCoords = (500, -100)
blankCoords = (500, 10, 400, 241)
moveLeftImageCoords = (450, -120)
moveRightImageCoords = (420, -120)
moveForwardImageCoords = (420, -100)
moveBackwardImageCoords = (320, -200)
moveUpImageCoords = (310, -200)
moveDownImageCoords = (310, -200)
successImageCoords = (430, 0)
numImageCoords = (500, -10)

digitImageCoords = (450, 450)
timesAttemptedCoords = (20,20)
timesComparedCoords = (20,400)
achievedCoords = [(20, 750),
                  (50, 750),
                  (80, 750),
                  (110, 750),
                  (140, 750),
                  (170, 750),
                  (200, 750),
                  (230, 750),
                  (260, 750),
                  (290, 750),
                  ]

# Progress bar increments
starCoords = (100,420)
greenInc = [(100,523,30,30), (100,486,30,30), (100,449,30,30)]
redInc = [(100,567,30,30), (100,604,30,30), (100,641,30,30)]
baseBar = (100,560,30,5)

coordVec = [(300,300), (-200,300)]
leaderboardCoords = (250, 400)

# where to display mode selection images
# boxCoords = [ xmin, xmax, ymin, ymax]
# boxRect = (left, top, width, height)
mathBox = (111,301)
#mathCoords = [-50, 300, 400, 300]
mathRect = (110, 300, 105, 105)

speedBox = (mathBox[0] + 250, 101)
#speedCoords = [400, 450, 400, 300]
speedRect = (360, 100, 105, 105)
timerCoords = (150, 500) #originally 100
clockCoords = ((timerCoords[0]-110), (timerCoords[1]-15))
correctCoords = (timerCoords[0], timerCoords[1]+200)
duringCheckCoords = (correctCoords[0]-70, correctCoords[1])


timeUpCoords = (300,100)
redZeroCoords = (timeUpCoords[0]+135, timeUpCoords[1]+20)
scoreCoords = (timeUpCoords[0]+10, timeUpCoords[1]+250)
checkCoords = (scoreCoords[0]-120, scoreCoords[1])
missedCoords = (scoreCoords[0], scoreCoords[1]+150)
redXCoords = (checkCoords[0], missedCoords[1])
speederboardCoords = (scoreCoords[0]+100, scoreCoords[1])


practiceBox = (speedBox[0] + 250, mathBox[1])
#practiceCoords = [400, 450, 400, 300]
practiceRect = (610, 300, 105, 105)


eqnCoords = (200,500)
ansCoords = (eqnCoords[0] + 300, eqnCoords[1]-7)

backBtnCoords = (60, 250)

# achievement coordinates
xSpacer = 50
ySpacer = 70

boxCoords = (110, 520, 250, 230)
trophyCoords = (10,520+70)

pbTagCoords = (boxCoords[0]+20, boxCoords[1]+5)
pb0Coords = (pbTagCoords[0]+ 1.3*xSpacer, pbTagCoords[1])
pb1Coords = (pb0Coords[0] + xSpacer, pb0Coords[1])
pb2Coords = (pb1Coords[0] + xSpacer, pb1Coords[1])

sb0Coords = (pb0Coords[0], pb0Coords[1]+ySpacer)
sb1Coords = (pb0Coords[0] + xSpacer, sb0Coords[1])
sb2Coords = (pb1Coords[0]+ xSpacer, sb0Coords[1])
sbTagCoords = (pbTagCoords[0], pbTagCoords[1]+ySpacer)

mb0Coords = (pb0Coords[0], sb0Coords[1]+ySpacer)
mb1Coords = (pb0Coords[0] + xSpacer, mb0Coords[1])
mb2Coords = (pb1Coords[0] + xSpacer, mb1Coords[1])
mbTagCoords = (pbTagCoords[0], sbTagCoords[1]+ySpacer)

# pbTagCoords = (boxCoords[0] + 5, boxCoords[1] + 180)
# pb0Coords = (pbTagCoords[0], pbTagCoords[1] - ySpacer)
# pb1Coords = (pb0Coords[0], pb0Coords[1] - ySpacer)
# pb2Coords = (pb1Coords[0], pb1Coords[1] - ySpacer)
#
# sbTagCoords = (pbTagCoords[0] + xSpacer, pbTagCoords[1])
# sb0Coords = (pb0Coords[0] + xSpacer, pb0Coords[1])
# sb1Coords = (pb0Coords[0] + xSpacer, sb0Coords[1] - ySpacer)
# sb2Coords = (pb1Coords[0] + xSpacer, sb1Coords[1] - ySpacer)
#
# mbTagCoords = (sbTagCoords[0] + xSpacer, pbTagCoords[1])
# mb0Coords = (sb0Coords[0] + xSpacer, sb0Coords[1])
# mb1Coords = (sb0Coords[0] + xSpacer, mb0Coords[1] - ySpacer)
# mb2Coords = (sb0Coords[0] + xSpacer, mb1Coords[1] - ySpacer)
#





# rectangle size of the white block that clears the others
clear = (-200, 300, 600, 300)



#Speed of circle movement
circleVelocity = 4

#Axis values
xMin = -600.0
xMax = 600.0
yMin = -600.0
yMax = 600.0

x = 0
y = 0


#Maybe make a class out of this later?