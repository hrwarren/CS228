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

#Where to display the helpful images
startingImageCoords = (500, -100)
blankCoords = (500, 10, 400, 241)
moveLeftImageCoords = (450, -120)
moveRightImageCoords = (420, -120)
moveForwardImageCoords = (420, -100)
moveBackwardImageCoords = (320, -200)
moveUpImageCoords = (310, -200)
moveDownImageCoords = (310, -200)
successImageCoords = (400, -70)
numImageCoords = (500, -10)
digitImageCoords = (350, 360)
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

coordVec = [(300,300), (-200,300)]

#rectangle size of the white block that clears the others
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