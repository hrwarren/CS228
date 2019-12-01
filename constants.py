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
lockCoords = (300, 100)
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
boardCoords = (250, 400)

# where to display mode selection images
# boxCoords = [ xmin, xmax, ymin, ymax]
# boxRect = (left, top, width, height)
mathBox = (111,301)
#mathCoords = [-50, 300, 400, 300]
mathRect = (110, 300, 105, 105)

speedBox = (mathBox[0] + 250, 101)
#speedCoords = [400, 450, 400, 300]
speedRect = (360, 100, 105, 105)
timerCoords = (100, 500)
timeUpCoords = (300,300)

scoreCoords = (timeUpCoords[0]+10, timeUpCoords[1]+100)
checkCoords = (scoreCoords[0]-120, scoreCoords[1])

missedCoords = (scoreCoords[0], scoreCoords[1]+150)
redXCoords = (checkCoords[0], missedCoords[1])


practiceBox = (speedBox[0] + 250, mathBox[1])
#practiceCoords = [400, 450, 400, 300]
practiceRect = (610, 300, 105, 105)



eqnCoords = (200,500)
ansCoords = (eqnCoords[0] + 300, eqnCoords[1]-7)

backBtnCoords = (60, 250)




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