# def Scale(coord, leapMin, leapMax, winMin, winMax):
#     screenwidth = winMax - winMin
#     scalar = 3
#     ratio = (((scalar * coord) + ((leapMax - leapMin) / 2)) / (leapMax - leapMin))
#     print(ratio)
#     return int((ratio) / (screenwidth))

def Scale(coord, leapMin, leapMax, winMin, winMax):  # this Min could be zero dammit
    screenwidth = winMax - winMin
    #scalar = 3 would normally multiply coord
    coordScaled = ((coord - (leapMax-leapMin)) * screenwidth) / (leapMax - leapMin)
    return(int(coordScaled))

    # def Scale(self, coord, leapMin, leapMax, winMin, winMax):  # this Min could be zero dammit
    #     screenwidth = winMax - winMin
    #     scalar = 2
    #     ratio = ((coord - (leapMax - leapMin)) / (winMax - winMin))
    #     #print(ratio)
    #     return(int(ratio))

x = 10
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