def Scale(coord, leapMin, leapMax, winMin, winMax):
    screenwidth = winMax - winMin
    scalar = 3
    ratio = (((scalar * coord) + ((leapMax - leapMin) / 2)) / (leapMax - leapMin))
    print(ratio)
    return int((ratio) / (screenwidth))


x = 50
leapMin = 0
leapMax = 100
winMin = 0
winMax = 1000

# 3*50 = 150
# leapMax - leapMin = 100
# 100/2 = 50
# 150 + 50 = 200
# 200/100 = 2

n = Scale(x, leapMin, leapMax, winMin, winMax)
print(n)