# import gestureDataFilenames
# #
# # path = 'C:\Users\Haley\Desktop\School Papers\HCI CS228 Jr\LeapDeveloperKit_3.2.1_win\LeapDeveloperKit_3.2.1+45911_win\LeapSDK\lib\CS228\Del6\userData'
# #
# # filenames = gestureDataFilenames.FILE_NAMES(path)
# #
# # filenames.Rename_Files(path)
# #
# # gestureDictionary = filenames.Make_Gesture_Dictionary(path)
# #
# # print(len(gestureDictionary))
import numpy as np

d = 0
y = np.zeros((20000, 1), dtype='f')

# while True:
#     for row in range(0, 1000):
# #    for d in range(0, 10):  # normally 0:10
#         if (d + 1) < 10:  # normally < 20
#             y[row + d*1000        ,0] = 0
#             y[(row + ((d+1)*1000)), 0] = 0
#             y[(row + ((d+2)*1000)), 0] = 0
#             y[(row + 3000), 0] = 1
#             y[(row + 4000), 0] = 1
#             y[(row + 5000), 0] = 1
#             y[(row + 6000), 0] = 2
#             y[(row + 7000), 0] = 2
#             y[(row + 8000), 0] = 2
#             y[(row + 9000), 0] = 3
#             y[(row + 10000), 0] = 3
#             y[(row + 11000), 0] = 3
#             y[(row + 12000), 0] = 4
#             y[(row + 13000), 0] = 4
#             y[(row + 14000), 0] = 4
#             y[(row + 15000), 0] = 5
#             y[(row + 16000), 0] = 5
#             y[(row + 17000), 0] = 5
#             y[(row + 18000), 0] = 6
#             y[(row + 19000), 0] = 6
#             y[(row + 20000), 0] = 6
#             y[(row + 21000), 0] = 7
#             y[(row + 22000), 0] = 7
#             y[(row + 23000), 0] = 7
#             y[(row + 24000), 0] = 8
#             y[(row + 25000), 0] = 8
#             y[(row + 26000), 0] = 8
#             y[(row + 27000), 0] = 9
#             y[(row + 28000), 0] = 9
#             y[(row + 29000), 0] = 9


#     print(y)
#     False


for d in range(0,10):
    for row in range(0,1000):
        for j in range (0,3):
        # y[(row + (d*1000)),0] = d #this works for 10k, but not for 20k
        # y[(row + ((d+1)*1000)), 0] = d
            y[row + (d+j)*1000        ,0] = d
        # y[(row + ((d+j+1)*1000)), 0] = d
        # y[(row + ((d+j+2)*1000)), 0] = d
exit()